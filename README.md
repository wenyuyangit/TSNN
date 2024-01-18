# TSNN
This repository contains the testing code of [A Deep Learning Solution for Height Estimation on
a Forested Area based on Pol-TomoSAR data](https://ieeexplore.ieee.org/abstract/document/10121647)., a FCN-based solution for height estimation of forested areas.

If you find this information helpful and choose to incorporate it into your research, please include the following citation:
> W. Yang, S. Vitale, H. Aghababaei, G. Ferraioli, V. Pascazio and G. Schirinzi, "A Deep Learning Solution for Height Estimation on a Forested Area Based on Pol-TomoSAR Data," in IEEE Transactions on Geoscience and Remote Sensing, vol. 61, pp. 1-14, 2023, Art no. 5208214, doi: 10.1109/TGRS.2023.3274395.


TSNN consists of several lays of FCN and the concept of using an FCN-based network for height estimation is from [TSNN for the urban](https://ieeexplore.ieee.org/abstract/document/8900616). 
<p align="center">
 <img src="images/workflow.png" width="800">
</p>

TSNN consists of nine fully connected layers with 400 neurons for the first eight layers while for the last one whose number of neurons matches the number of considered classes. All the layers, but the last, are followed by the [Rectified Linear Unit (ReLU)](https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) activation function that ensures a stable training procedure and fast convergence.

<p align="center">
<img src="images/architecture.png" width=380> 
</p>

The cost function is the multiclass cross-entropy function (CE).

<p align="center">
<img src="images/ce.png" width=450> 
</p>


An example on simulated data is shown below
Noisy Image| Noise-Free Reference | InSAR-MONet 
:-----------------------------------------|:---------------------------------------:|:--------------------------------------:
<img src="https://user-images.githubusercontent.com/36993034/197556940-3af2a154-d82d-4df3-b18d-bd37b0258bd7.png" width="150"> |<img src="https://user-images.githubusercontent.com/36993034/197557009-a407aea1-8f7c-41a5-834c-87066edace1e.png" width="150"> |<img src="https://user-images.githubusercontent.com/36993034/197557074-e7566a82-f0bf-4853-9776-8ef22aa77c82.png" width="150">

# Team members
 Wenyu Yang (contact person, wenyu.yang001@studenti.uniparthenope.it); \
 Sergio Vitale (sergio.vitale@uniparthenope.it);
 Hossein Aghababaei (h.aghababaei@utwente.nl);
 Giampaolo Ferraioli (giampaolo.ferraioli@uniparthenope.it);
 Vito Pascazio (vito.pascazio@uniparthenope.it);
 Gilda  Schirinzi (gilda.schirinzi@uniparthenope.it)

 
# License (how to get it ? for Sergio)
Copyright (c) 2022 Dipartimento di Ingegneria and Dipartimento di Scienze e Tecnologie of Università degli Studi di Napoli "Parthenope".

All rights reserved. This work should only be used for nonprofit purposes.

By downloading and/or using any of these files, you implicitly agree to all the
terms of the license, as specified in the document LICENSE.txt
(included in this directory)

# Usage 
* **data** folder contains three sample images with simulated interferometric SAR phases (corresponding to the examples of the paper);
Three different cases can be tested:
     * small baseline and high coherence (B1, Gamma 4)
     * medium baseline and medium coherence (B2, Gamma 3)
     * large baseline and low coherence (B4, Gamma 1)

* *model* contains trained weights
* *model.py* contains the model implementation
* *testing.py* is the main script for testing

# Prerequisites
This code is written on the Ubuntu system for Python 3.7 and uses the Pytorch library.

For correct usage of the code, please install the Python environment saved in **./env/monet_pytorch.yml** with the following step:

**Installing Anaconda** (if not already installed)

1. download anaconda3 from https://www.anaconda.com/products/individual#linux
2. from the command line, move to the download directory and install the package by:
> sh <Anaconda_downloaded_version>.sh 
and follow the instructions for installation
3. add conda to path
> PATH=~/anaconda3/bin:$PATH

**Installing the conda environment**

The file ./insarmonet_env.yml contains the environment for testing the code. You can easily install it by command line:

1. move to the folder containing the GitHub repository and open the terminal
2. run the following command
 > conda env create -f insarmonet_env.yml


Once the environment has been set up, activate it by command line as well:

1. activate the environment from the command line

> conda activate insarmonet_env

2. Launch Spyder

> spyder

3. goes to the folder containing **testing.py**, edit, and run



