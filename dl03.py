import os
import pandas as pd
import torch

a=torch.ones((2,5,4))
print(a.shape)
print(a.sum(axis=[0,2]).shape)

