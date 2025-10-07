#Scalars
x=25
print(type(x))
y=3.5
print(type(x+y))

import torch
x_pt=torch.tensor(25)
print(x_pt.shape)

import tensorflow as tf
x_tf=tf.Variable(35)
print(type(x_tf))
print(x_tf.shape)

#y_tf=tf.Variable(3,dtype=tf.int16) <-- this throws error because x_tf is int32 by default
y_tf=tf.Variable(3,dtype=tf.int32)
print(type((x_tf+y_tf).numpy()))
#print(type(y+x_tf)) <-- this one throws an error


#Vectors
