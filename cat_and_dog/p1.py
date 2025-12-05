import torch
def activation(x):
    return 1/(1+torch.exp(-x))

# features=torch.randn(1,5)
# weights=torch.randn_like(features)
# bias=torch.randn(1,1)
# y=activation(torch.mm(features,weights.view(5,1))+bias)
# print(y)
torch.manual_seed(7)
features=torch.randn(1,3)
n_inputs=features.shape[1]
n_hidden=2
n_output=1
W1=torch.randn(n_inputs,n_hidden)
W2=torch.randn(n_hidden, n_output)
B1=torch.randn((1,n_hidden))
B2=torch.randn((1,n_output))
y1=activation(torch.mm(features,W1)+B1)
y2=activation(torch.mm(y1,W2)+B2)
print(y2)
