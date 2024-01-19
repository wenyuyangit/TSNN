#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:20:41 2022

@author: wenyu
"""
from TSNN_cov_models_CHM import *
import torch
import matplotlib.pyplot as plt
import numpy as np
import scipy.io

# parametersClasses = 37   # 10  14  20  40 79 131
Layers = 9
Nnodes = 400
Classes = 37
Lr = 0.0001
ifcali = 'nc' # nc,c, phase calibrated or not
print('Layers:',Layers)
print('Nnodes:',Nnodes)


#%%
modelpath = 'CHM_'+str(Layers)+'layer_' +str(Nnodes)+'_'+str(Lr)+'_'+ifcali+'_para.pth' # CHM_9layer_400_0.0001_nc_para.pth
net  = TSNNnet(input_channels = 52, nnodes = Nnodes, classes = Classes, layers = Layers)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
net.load_state_dict(torch.load(modelpath, map_location=device))
# net.load_state_dict(torch.load( modelpath ))
#%% functions

patch_x = np.load('CHM_patch1_x_'+ifcali+'.npy')
patch_y = np.load('CHM_patch1_y_step1.npy')

print(patch_x.size)
print(patch_y.size)
    
file_name = 'Patch1_CHM_'+str(Layers)+'layer_' +str(Nnodes)+'_'+str(Lr)+'_'+ifcali+'.mat'
 
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
# plt.imshow(np.reshape(y_ref,(300,300)),interpolation='none')
# plt.title('Reference Height')
# plt.clim(0,37)
# plt.colorbar(cmap='jet')
# plt.show()

# plt.figure(2)
# plt.imshow(np.reshape(y_pred,(300,300)),interpolation='none')
# plt.title('Predicted Height')
# plt.clim(0,37)
# plt.colorbar(cmap='jet')
# plt.show()
