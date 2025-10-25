import numpy as np
import torch

norm=np.linalg.norm

def tensor_vs_numpy_norm():
    '''Demonstrate interoperability of numpy and torch norm functions'''
    tx=torch.tensor([[1,2],[3,4]])
    #note below--> np function is able to process torch object
    print(norm(tx))

    nx=np.arange(9).reshape(3,3)
    try:
        print(torch.norm(nx))
    except Exception as e:
        print("torch.norm function is not able to process np object")
        print(e)

    print(norm(nx))

    nu=np.ones((5,5))
    print(nu)
    print(norm(nu))

def torch_norm():
    tu=torch.ones((4,4))
    print(torch.norm(tu))
    print(torch.norm(tu,dim=1)) #dim=-2 works but dim=2 does not, why?

def test_norm_x1():
    x1=np.array([12,4,7])
    print('x1 is :',x1)
    print('norm(x1) is :',norm(x1))
    print('sqrt(x[0]^2+x[1]^2+x[2]^2) is :',(12**2+4**2+7**2)**0.5)


def test_norm_x2(x2):
    print('norm(x2) is :',norm(x2))
    print('sqrt(x2[0]**2+x2[1]**2+x2[2]**2) is :',(x2[1]**2+x2[1]**2+x2[2]**2)**0.5)
    #x2=x2.T
    print('sqrt(norm(x2[0])**2+norm(x2[1])**2+norm(x2[2])**2) is :',
        (norm(x2[1])**2+norm(x2[1])**2+norm(x2[2])**2)**0.5)

print("\nnorm when shape is (3,4)")
x2=np.arange(12).reshape(3,4)
print('x2 is : \n',x2)
test_norm_x2(x2)

print("\nnorm when shape is (4,3)")
x2=np.arange(12).reshape(4,3)
print('x2 is : \n',x2)
test_norm_x2(x2)