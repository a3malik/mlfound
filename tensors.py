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

def tensorflow_scalar():
    import tensorflow as tf
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
def _1D_array():
    x=np.array([4,5,6]) #does this vector represent a point in 3D space?
    print("shape of [1,2,3] and [1,2,3].T")
    print(x.shape)
    print(x.T.shape)

#Transpose of a 2D array
def _2D_array():
    x=np.array([[4,5],[5,6],[6,7]])
    print(x,x.shape)
    print(x.T,x.T.shape)

#How are 1D arrays different from vactors? Is 2D array a vector?

def _1D_and_2D_vectors():
    '''np.array can create a 1D as well as 2D vector, why do we call a 2D array a 2D vector?
    for a 2D array to be a vector it should have only one column or one row'''
    _1d_vector=np.array([22,8,4])
    _2d_vector=np.array([[22,8,4]])
    print("details of 1D vectors")
    print(_1d_vector,_1d_vector.shape, _1d_vector.T.shape)
    print("details of 2D vectors")
    print(_2d_vector,_2d_vector.shape, _2d_vector.T.shape)
#_1D_and_2D_vectors()

def zero_vectors():
    x=np.zeros(3)
    print(x,x.shape)
    x=np.zeros((3,4))
    print(x,x.shape)
#zero_vectors()

def torch_vectors():
    x=torch.tensor([11,4,2])
    print(x,x.shape)
    #print(x.T,x.T.shape) <-- Throws a warning
    print(type(x))
#torch_vectors()

def tf_vectors():
    from tensorflow import Variable
    x=Variable([11,4,2])
    print(x,x.shape)
    #print(x.T,x.T.shape) <--Throws an error
    print(type(x))
#tf_vectors()