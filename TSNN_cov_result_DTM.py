#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:20:41 2022

@author: wenyu
"""
from TSNN_cov_models_DTM import *
import torch
import matplotlib.pyplot as plt
import numpy as np

# parameter
Classes = 37
Layers = 9
Nnodes = 400
Lr = 0.0001
ifcali = 'nc' # nc,c
print('Layers:',Layers)
print('Nnodes:',Nnodes)


#%% load trained network
modelpath = 'DTM_'+str(Layers)+'layer_' +str(Nnodes)+'_'+str(Lr)+'_'+ifcali+'_para.pth' # CHM_9layer_400_0.0001_nc_para.pth
net  = TSNNnet(input_channels = 52, nnodes = Nnodes, classes = Classes, layers = Layers)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
net.load_state_dict(torch.load(modelpath, map_location=device))
# net.load_state_dict(torch.load( modelpath ))

# load data
patch_x = np.load('DTM_patch2_x_'+ifcali+'.npy')
patch_y = np.load('DTM_patch2_y_step1.npy')

print(patch_x.size)
print(patch_y.size)

file_name = 'Patch2_DTM_'+str(Layers)+'layer_' +str(Nnodes)+'_'+str(Lr)+'_'+ifcali+'.mat'
 
test_x = torch.from_numpy(patch_x)
test_y = torch.from_numpy(patch_y)


outputs = net(test_x)
_,predictions = torch.max(outputs.data,1)

y_ref = test_y.numpy()
y_pred = predictions.numpy()
y_ref[y_ref>37] = -1

# save to .mat
data = {'labels':y_ref,'pred':y_pred}

scipy.io.savemat(file_name,data)


# plt.figure(1)
# plt.imshow(np.reshape(y_ref.numpy(),(300,300)),interpolation='none')
# plt.show()

# plt.figure(2)
# plt.imshow(np.reshape(y_pred.numpy(),(300,300)),interpolation='none')
# plt.show()
