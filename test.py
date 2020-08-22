import torch
name = 'Mitchell'
age = 24
print(f'my name is {name} and my age is {age}')

print('\b\b\r')

print("hello")

dataset_size = 1000
batch_size = 10

input = torch.rand(batch_size, 3, 192, 192)
target = torch.ones(batch_size, 1, 192, 192)
data = [(input, target)] * (dataset_size // batch_size)

print(data)
a = 10