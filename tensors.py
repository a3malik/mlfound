#Scalars
def ordinary_scalars():
    x=25
    print(type(x))
    y=3.5
    print(type(x+y))

import torch
def torch_scalars():
    x_pt=torch.tensor(25)
    print(x_pt.shape)

import tensorflow as tf
def tensorflow_scalar():
    x_tf=tf.Variable(35)
    print(type(x_tf))
    print(x_tf.shape)

    #y_tf=tf.Variable(3,dtype=tf.int16) <-- this throws error if we add it to x_tf
    # because x_tf is int32 by default
    y_tf=tf.Variable(3,dtype=tf.int32)
    print(type((x_tf+y_tf).numpy()))
    #print(type(y+x_tf)) <-- this one throws an error


#Vectors
import numpy as np
def vector_prints():
    x=np.array([25,2,5])
    print("length of x is ",len(x))
    print("shape of x is ",x.shape)
    x=np.array([[12,2,9],[3,14,7]],dtype=np.float16)
    print("Now new shape of x is ",x.shape)
    print("type of x is ",type(x))
    print("datatype of x is ",type(x.T[:,1][2]))

#Transpose of a regular 1D array
x=np.array([4,5,6]) #does this vector represent a point in 3D space?
print("shape of [1,2,3] and [1,2,3].T")
print(x.shape)
print(x.T.shape)

#Transpose of a 2D array
x=np.array([[4,5],[5,6],[6,7]])
print(x,x.shape)
print(x.T,x.T.shape)

#How are 1D arrays different from vactors? Is 2D array a vector?

def _1D_and_2D_vectors():
    '''np.array can create a 1D as well as 2D vector, why do we call a 2D array a 2D vector?
    for a 2D array to be a vector it should have only one column or one row'''
    _1d_vector=np.array([22,8,4])
    _2d_vector=np.array([[22,8,4]])
    print(_1d_vector,_1d_vector.shape, _1d_vector.T.shape)
    print(_2d_vector,_2d_vector.shape, _2d_vector.T.shape)
_1D_and_2D_vectors()