import torch.nn as nn


class ConvBNReLU(nn.Module):
    """3x3 Conv + BN + ReLU"""
    def __init__(self, in_channels, out_channels):
        super(ConvBNReLU, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1)  # why padding 1?
        self.bn = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)   # inplace?

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        return x
