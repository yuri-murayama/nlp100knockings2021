import torch
import torch.nn as nn

## 多層ニューラルネットワーク
class Multi_Layer_NN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, bias=True):
        super(Multi_Layer_NN, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, hidden_size, bias=bias),
            nn.BatchNorm1d(hidden_size),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_size, output_size, bias=bias)
        )

    def forward(self, x):
        x = self.net(x)
        return x