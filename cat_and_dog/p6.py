# 
from torchvision import datasets,transforms
from torch import nn, optim
import torch

class Network(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden1=nn.Linear(784,256)
        self.hidden2=nn.Linear(256,128)
        self.hidden3=nn.Linear(256,64)
        self.output=nn.Linear(64,10)
        self.ReLU=nn.ReLU()
        self.softmax=nn.Softmax(dim=1)
    def forward(self,x):
        x=x.view(x.shape[0],-1)
        x=self.relu(self.hidden1(x))
        x=self.relu(self.hidden2(x))
        x=self.relu(self.hidden3(x))
        x=self.log_softmax(self.output(x),dim=1)
        return x

transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,),(0.5,)),])
trainset=datasets.MNIST('Fashion-MNIST/', download=True, train=True, transform=transform)
trainloader=torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
model= Network()
criterion=nn.NLLLoss()
optimizer=optim.Adam(model.parameters(),lr=0.003)
epochs=30
steps=0
train_losses, test_losses=[],[]
for e in range(epochs):
    running_loss=0
    for images,labels in trainloader:
        optimizer.zero_grad()
        logps=model(images)
        loss=criterion(logps,labels)
        loss.backward()
        optimizer.step()
        running_loss+=loss.item()
    else:
        test_loss=0
        accuracy=0
        with torch.no_grad():
            for images, labels in trainoader:
                logps=model(images)
                test_loss+=criterion(logps,labels)
                ps=torch.exp(logps)
                top_p,top_class=ps.topk(1, dim=1)
                equals=top_class==labels.view(*top_class.shape)
                accuracy+=torch.mean(equals.type(torch.FloatTensor))
        train_losses.append(running_loss/len(trainloader))
        test_losses.append(test_loss/len(testloader))

        print(f"Training loss{running_loss}")
dataiter=iter(trainloader)
images,labels=dataiter.next()
img=images[1]

ps=torch.exp(model(img))
helper.view_classify(img,ps,version="Fashion")