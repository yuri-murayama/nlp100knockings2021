import torch
import torch.nn as nn
import pandas as pd

## 単層ニューラルネットワーク
class Single_Layer_NN(nn.Module):
    def __init__(self, input_size, output_size, bias=False):
        super(Single_Layer_NN, self).__init__()
        self.fc = nn.Linear(input_size, output_size, bias=bias)

    def forward(self, x):
        x = self.fc(x)
        return x

if __name__ == '__main__':
    X_train = pd.read_table('data/X_train.txt')
    X_train = torch.tensor(X_train.values, dtype=torch.float)
    Y_train = pd.read_table('data/Y_train.txt')
    Y_train = torch.squeeze(torch.tensor(Y_train.values, dtype=torch.long))

    model = Single_Layer_NN(300, 4)
    loss = nn.CrossEntropyLoss()
    for i in [1, 4]:
        pred = model(X_train[:i])
        y = nn.Softmax(dim=1)(pred)
        l = loss(pred, Y_train[:i])
        model.zero_grad()
        l.backward()
        print('各カテゴリに属する確率\n', y)
        print('Loss\n', l)
        print('勾配\n', model.fc.weight.grad)

'''
（実行結果）
各カテゴリに属する確率
 tensor([[0.2379, 0.2721, 0.2355, 0.2545]], grad_fn=<SoftmaxBackward>)
Loss
 tensor(1.4458, grad_fn=<NllLossBackward>)
勾配
 tensor([[ 0.0569,  0.0393, -0.0105,  ..., -0.0262,  0.0244, -0.0288],
        [ 0.0650,  0.0449, -0.0120,  ..., -0.0300,  0.0279, -0.0330],
        [-0.1827, -0.1262,  0.0336,  ...,  0.0843, -0.0785,  0.0927],
        [ 0.0608,  0.0420, -0.0112,  ..., -0.0281,  0.0261, -0.0309]])
各カテゴリに属する確率
 tensor([[0.2379, 0.2721, 0.2355, 0.2545],
        [0.2400, 0.2660, 0.2360, 0.2580],
        [0.2429, 0.2471, 0.2579, 0.2520],
        [0.2527, 0.2500, 0.2601, 0.2372]], grad_fn=<SoftmaxBackward>)
Loss
 tensor(1.4186, grad_fn=<NllLossBackward>)
勾配
 tensor([[ 0.0135,  0.0205,  0.0011,  ..., -0.0191,  0.0093,  0.0048],
        [ 0.0158, -0.0126,  0.0010,  ...,  0.0010, -0.0041, -0.0095],
        [-0.0451, -0.0245,  0.0046,  ...,  0.0228, -0.0155,  0.0178],
        [ 0.0157,  0.0167, -0.0066,  ..., -0.0047,  0.0103, -0.0130]])   
'''