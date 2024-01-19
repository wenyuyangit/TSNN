#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 18:44:09 2022

@author: wenyu
"""

# from sklearn.metrics import confusion_matrix

import torch
# import torchvision
# import torchvision.transforms as transforms

import matplotlib.pyplot as plt
import numpy as np

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
# from pretty_confusion_matrix import pp_matrix_from_data

import scipy.io

def TSNNnet(input_channels, nnodes, classes, layers):
    class Net_4L(nn.Module):  
        def __init__(self):
            super().__init__()
            self.fc1 = nn.Linear(input_channels,nnodes)
            self.fc2 = nn.Linear(nnodes,nnodes)
            self.fc3 = nn.Linear(nnodes,nnodes)
            self.fc4 = nn.Linear(nnodes,classes)
        def forward(self,x):
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = F.relu(self.fc3(x))
            x = self.fc4(x)
            return x
        
    class Net_5L(nn.Module):  
        def __init__(self):
            super().__init__()
            self.fc1 = nn.Linear(input_channels,nnodes)
            self.fc2 = nn.Linear(nnodes,nnodes)
            self.fc3 = nn.Linear(nnodes,nnodes)
            self.fc4 = nn.Linear(nnodes,nnodes)
            self.fc5 = nn.Linear(nnodes,classes)
        def forward(self,x):
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = F.relu(self.fc3(x))
            x = F.relu(self.fc4(x))
            x = self.fc5(x)
            return x
        
        
    class Net_6L(nn.Module):  
        def __init__(self):
            super().__init__()
            self.fc1 = nn.Linear(input_channels,nnodes)
            self.fc2 = nn.Linear(nnodes,nnodes)
            self.fc3 = nn.Linear(nnodes,nnodes)
            self.fc4 = nn.Linear(nnodes,nnodes)
            self.fc5 = nn.Linear(nnodes,nnodes)
            self.fc6 = nn.Linear(nnodes,classes)
        def forward(self,x):
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = F.relu(self.fc3(x))
            x = F.relu(self.fc4(x))
            x = F.relu(self.fc5(x))
            x = self.fc6(x)
            return x
        
        
    class Net_7L(nn.Module):  # 1FC+1RELU
        def __init__(self):
            super().__init__()
            self.fc1 = nn.Linear(input_channels,nnodes)
            self.fc2 = nn.Linear(nnodes,nnodes)
            self.fc3 = nn.Linear(nnodes,nnodes)
            self.fc4 = nn.Linear(nnodes,nnodes)
            self.fc5 = nn.Linear(nnodes,nnodes)
            self.fc6 = nn.Linear(nnodes,nnodes)
            self.fc7 = nn.Linear(nnodes,classes)
        def forward(self,x):
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = F.relu(self.fc3(x))
            x = F.relu(self.fc4(x))
            x = F.relu(self.fc5(x))
            x = F.relu(self.fc6(x))
            x = self.fc7(x)
            return x
        
        
    class Net_8L(nn.Module):  # 1FC+1RELU
        def __init__(self):
            super().__init__()
            self.fc1 = nn.Linear(input_channels,nnodes)
            self.fc2 = nn.Linear(nnodes,nnodes)
            self.fc3 = nn.Linear(nnodes,nnodes)
            self.fc4 = nn.Linear(nnodes,nnodes)
            self.fc5 = nn.Linear(nnodes,nnodes)
            self.fc6 = nn.Linear(nnodes,nnodes)
            self.fc7 = nn.Linear(nnodes,nnodes)
            self.fc8 = nn.Linear(nnodes,classes)
        def forward(self,x):
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = F.relu(self.fc3(x))
            x = F.relu(self.fc4(x))
            x = F.relu(self.fc5(x))
            x = F.relu(self.fc6(x))
            x = F.relu(self.fc7(x))
            x = self.fc8(x)
            return x
        
    class Net_9L(nn.Module):  # 1FC+1RELU
        def __init__(self):
            super().__init__()
            self.fc1 = nn.Linear(input_channels,nnodes)
            self.fc2 = nn.Linear(nnodes,nnodes)
            self.fc3 = nn.Linear(nnodes,nnodes)
            self.fc4 = nn.Linear(nnodes,nnodes)
            self.fc5 = nn.Linear(nnodes,nnodes)
            self.fc6 = nn.Linear(nnodes,nnodes)
            self.fc7 = nn.Linear(nnodes,nnodes)
            self.fc8 = nn.Linear(nnodes,nnodes)
            self.fc9 = nn.Linear(nnodes,classes)
        def forward(self,x):
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = F.relu(self.fc3(x))
            x = F.relu(self.fc4(x))
            x = F.relu(self.fc5(x))
            x = F.relu(self.fc6(x))
            x = F.relu(self.fc7(x))
            x = F.relu(self.fc8(x))
            x = self.fc9(x)
            return x
    if (layers == 4):
        model = Net_4L()
    elif (layers == 5):
        model = Net_5L()
    elif(layers == 6):
        model = Net_6L()
    elif(layers == 7):
        model = Net_7L()
    elif(layers == 8):
        model = Net_8L()
    elif(layers == 9):
        model = Net_9L()
            
        
 
    return model
    