import numpy as np
import torch

norm=np.linalg.norm
tx=torch.tensor([[1,2],[3,4]])
#note below--> np function is able to process torch object
print(norm(tx))

nx=np.arange(9).reshape(3,3)
try:
    print(torch.norm(nx))
except Exception as e:
    print("torch.norm function is not able to process np object")
    print(e)

nu=np.ones((5,5))
print(nu)
print(norm(nu))

tu=torch.ones((4,4))
print(torch.norm(tu))
print(torch.norm(tu,dim=1)) #dim=-2 works but dim=2 does not, why?