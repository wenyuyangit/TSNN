# INSAR-MONet
This repository contains the testing code of **InSAR-MONet**, a CNN based solution for Interferometric SAR Phase denoising.

if you find it usefule and use it for you research, please cite as the following [InSAR-MONet: Interferometric SAR phase
denoising using a multi-objective neural network](mettere citazione).



InSAR-MONet inherits the 17 layers CNN architectures and the concept of using a multi-objective cost function from [MONet](https://ieeexplore.ieee.org/document/9261137). 

![net](https://user-images.githubusercontent.com/36993034/197556012-74be765f-48e6-44e9-85d6-b706a9928611.png)
The cost function is composed of three terms taking care of spatial and statistical properties of the interferometric phase: a cosine based metric for evaluating similarity between output and reference, a gradient based metric for edges preservation and the Kullback-Leibler divergence between estimated noise distribution and the theoretical one.

![cost](https://user-images.githubusercontent.com/36993034/197556133-3ce13133-b3ec-4913-a8a9-0ead333e6c7e.png)
![cost2](https://user-images.githubusercontent.com/36993034/197556216-307418ae-1cd4-4734-b837-61ed111f93d3.png)

An example on simulated data is shown below
Noisy Image| Noise-Free Reference | MONet - Output 
-----------------------------------------|---------------------------------------|--------------------------------------
![immagine](https://user-images.githubusercontent.com/36993034/197556940-3af2a154-d82d-4df3-b18d-bd37b0258bd7.png) |![immagine](https://user-images.githubusercontent.com/36993034/197557009-a407aea1-8f7c-41a5-834c-87066edace1e.png) |![immagine](https://user-images.githubusercontent.com/36993034/197557074-e7566a82-f0bf-4853-9776-8ef22aa77c82.png)

# Team members
 Sergio Vitale    (contact person, sergio.vitale@uniparthenope.it);
 Giampaolo Ferraioli (giampaolo.ferraioli@uniparthenope.it);
 Gilda  Schirinzi (gilda.schirinzi@uniparthenope.it)
 Vito Pascazio (vito.pascazio@uniparthenope.it)
 
# License
Copyright (c) 2022 Dipartimento di Ingegneria and Dipartimento di Scienze e Tecnologie of Università degli Studi di Napoli "Parthenope".

All rights reserved. This work should only be used for nonprofit purposes.

By downloading and/or using any of these files, you implicitly agree to all the
terms of the license, as specified in the document LICENSE.txt
(included in this directory)

# Prerequisits
This code is written on Ubuntu system for Python3.7 and uses Pytorch library.

INSERISCI ENVIRONMENT


# Usage 
* **data** folder contains three samples images with simulated interferometric SAR phases (corresponding to the examples of the paper);
Three differente cases can be tested:
     * small baseline and high coherence (B1, Gamma 4)
     * medium baseline and medium coherence (B2, Gamma 3)
     * large baseline and low coherence (B4, Gamma 1)

* *model* contains trained weigths
* *model.py* contains the model implementation
* *testing.py* is the main script for testing
