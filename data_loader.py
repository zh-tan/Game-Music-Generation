from torchvision import datasets, transforms
from torch.utils.data import DataLoader, TensorDataset
import torch
import torch.utils as utils
import numpy as np

transform = transforms.Compose([
    transforms.ToTensor()
])


def get_loader(directory='./datasets', batch_size=128, train=True, num_workers=1,
               pin_memory=True):
    # 32 x 32
    """dataset = datasets.CIFAR10(directory,
                               train=train,
                               download=True,
                               transform=transform)
    shuffle = not train
    loader = DataLoader(dataset,
                        batch_size=batch_size,
                        num_workers=num_workers,
                        shuffle=shuffle,
                        pin_memory=False)
    return loader"""
    x = np.load("data.npy")
    tensor_x = torch.Tensor(x)
    mydata = TensorDataset(tensor_x)
    my_dataloader = DataLoader(mydata, batch_size=batch_size)
    return my_dataloader
