import torch
from torch import nn
import torch.nn.functional as F
from torchvision import datasets,transforms
transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,),(0.5,)),])
trainset=datasets.MNIST('MNIST_data/', download=True, train=True, transform=transform)
trainloader=torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
model= nn.Sequential(nn.Linear(784,128),
nn.ReLU(),
nn.Linear(128,64),
nn.ReLU(),
nn.Linear(64,10),
nn.LogSoftmax(dim=1))
#criterion=nn.CrossEntropyLoss()
criterion=nn.NLLLoss()
images, labels=next(iter(trainloader))
images=images.view(images.shape[0],-1)
logits=model(images)
loss=criterion(logits, labels)
# print(f"Befre backward pass{model[0].weight.grad}")
# loss.backward()
print(loss)


# x=torch.randn(2,2,requires_grad=True)
# y=x**2
# print(y.grad_fn)
# z=y.mean()
# z.backward()
# from torch import optim
# optimizer=optim.SGD(model.parameters(), lr=0.01)