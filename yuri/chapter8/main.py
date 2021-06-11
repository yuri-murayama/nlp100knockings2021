import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
import os
import pandas as pd
from SLNN71_72 import Single_Layer_NN
from MLNN79 import Multi_Layer_NN
from torch.utils.tensorboard import SummaryWriter
import numpy as np
import time
import hydra

@hydra.main(config_path="config.yaml")
def main(cfg):
    owd = hydra.utils.get_original_cwd()

    def get_dataset(data):
        x = pd.read_table(os.path.join(owd, f'data/X_{data}.txt'))
        x = torch.tensor(x.values, dtype=torch.float)
        y = pd.read_table(os.path.join(owd, f'data/Y_{data}.txt'))
        y = torch.squeeze(torch.tensor(y.values, dtype=torch.long))
        return TensorDataset(x, y)

    train_dataset = get_dataset('train')
    valid_dataset = get_dataset('valid')
    test_dataset = get_dataset('test')

    ## GPUかCPUかチェック
    gpu = torch.cuda.is_available()
    device = torch.device("cuda") if gpu else torch.device("cpu")

    train_loader = DataLoader(train_dataset, batch_size=cfg.batch_size, shuffle=True, pin_memory=gpu)
    if cfg.model == 'SLNN':
        model = Single_Layer_NN(300, 4).to(device)
    else:
        model = Multi_Layer_NN(300, 200, 4).to(device)
    loss = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-1, momentum=0.9)
    writer = SummaryWriter()
    os.makedirs(os.path.join(owd, "save"), exist_ok=True)

    def evaluate(dataset):
        loader = DataLoader(dataset, batch_size=cfg.evaluation_batch_size, shuffle=False, pin_memory=gpu)

        model.eval()
        total, correct, l = 0, 0, 0
        with torch.no_grad():
            for x, y in loader:
                x = x.to(device)
                y = y.to(device)
                output = model(x)
                l += loss(output, y).item()
                output = torch.argmax(output, dim=1)
                correct += (output == y).sum().item()
                total += len(x)
            acc = correct / total
            mean_loss = l / len(loader)

        return acc, mean_loss

    ## 学習
    for epoch in range(cfg.num_epochs):
        start = time.time()
        train_loss = 0
        model.train()
        for i, (x, y) in enumerate(train_loader):
            x = x.to(device)
            y = y.to(device)
            optimizer.zero_grad()
            pred = model(x)
            l = loss(pred, y)
            l.backward()
            optimizer.step()

            train_loss += l.item()

        print(f"Epoch:{epoch+1}, Train loss:{train_loss/(i+1):.4f}, Time:{time.time()-start}s")

        ## 訓練データでの損失、正解率をプロット
        train_acc, train_loss = evaluate(train_dataset)
        writer.add_scalar('Accuracy/Train', train_acc, epoch)
        writer.add_scalar('Loss/Train', train_loss, epoch)

        ## 検証データでの損失、正解率をプロット
        valid_acc, valid_loss = evaluate(valid_dataset)
        writer.add_scalar('Accuracy/Valid', valid_acc, epoch)
        writer.add_scalar('Loss/Valid', valid_loss, epoch)

        ## チェックポイント保存
        checkpoint = {'epoch': epoch, 'model_state_dict': model.state_dict(), 'optimizer_state_dict': optimizer.state_dict()}
        torch.save(checkpoint, os.path.join(owd, f'save/checkpoint{epoch+1}.pt'))

    ## 評価データでの正解率
    test_acc, _ = evaluate(test_dataset)
    print('Accuracy/Test ', test_acc)

    writer.close()

if __name__ == '__main__':
    main()

# 単層ニューラルネットワークで実験
# python main.py > SLNN.log
# Accuracy/Test  0.9062265566391597

# バッチサイズを変えて1エポックにかかる時間を比較
# python main.py -m num_epochs=1 batch_size=1,2,4,8,16,32,64,128,256,512 > Batch.log

# 多層ニューラルネットワークで実験
# python main.py model=MLNN > MLNN.log
# Accuracy/Test  0.9204801200300075 (上がった！)
