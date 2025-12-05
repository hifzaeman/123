import torch
import numpy as np

import matplotlib.pyplot as plt
from torchvision import datasets, transforms
transform= transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5,),(0.5,)),])
trainset=datasets.MNIST('MNIST_data/', download=True, train=True, transform=transform)
trainloader=torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

dataiter = iter(trainloader)
images, labels = next(dataiter)
print(type(images))
print(images.shape)
print(labels.shape)

plt.imshow(images[1].numpy().squeeze(), cmap='Greys_r')

def activation(x):
    return 1/(1+torch.exp(-x))
def softmax(x):
    return torch.exp(x)/torch.sum(torch.exp(x),dim=1).view(-1,1)

inputs=images.view(images.shape[0], -1)
w1=torch.randn(784,256)
b1=torch.randn(256)
w2=torch.randn(256,10)
b2=torch.randn(10)
h=activation(torch.mm(inputs,w1)+b1)
o=(torch.mm(h,w2)+b2)
print(o.shape)
