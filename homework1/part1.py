import sys
import os
import numpy as np
from scipy import signal
import math
import random
import cv2
import run
from scipy import signal

def make_gaussian(k, std):
  '''Create a gaussian kernel.
  
  Input:

  k - the radius of the kernel.
  
  std - the standard deviation of the kernel.
  
  Output:

  output - a numpy array of shape (2k+1, 2k+1) and dtype float.
  
  If gaussian_1d is a gaussian filter of length 2k+1 in one dimension, 
  kernel[i,j] should be filled with the product of gaussian_1d[i] and 
  gaussian_1d[j].
 
  Once all the points are filled, the kernel should be scaled so that the sum
  of all cells is equal to one.'''
  '''
in c# code
  double[,] kernel = new double[size, size];

            // compute kernel
            for ( int y = -r, i = 0; i < size; y++, i++ )
            {
                for ( int x = -r, j = 0; j < size; x++, j++ )
                {
                    kernel[i, j] = Function2D( x, y );
                }
            }

            Math.Exp( ( x * x + y * y ) / ( -2 * sqrSigma ) ) / ( 2 * Math.PI * sqrSigma )
'''
  '''
for i in range(-rows/2+1,rows/2-1):
    for j in range(-rows/2+1,rows/2-1):
      kernel[i,j] = gaussian_1d[i]*gaussian_1d[j]

  kernel = kernel/kernel.sum()
'''
  kernel = None
  # Insert your code here.----------------------------------------------------
  #gaussian_1d = signal.gaussian(k,std)
  kernelsize = 2*k+1
  sqrSigma = std*std
  gaussian_1d = signal.gaussian(kernelsize,std)
  kernel = np.zeros((kernelsize,kernelsize),dtype=np.float64)
  for x in range(-k, k+1):
    for y in range(-k, k+1):
      #kernel[x+k,y+k]=math.exp(( x * x + y * y )/( -2 * sqrSigma ))/( 2 * math.pi * sqrSigma )
      kernel[x,y] = gaussian_1d[x]*gaussian_1d[y]


  kernel = kernel/kernel.sum()
  #---------------------------------------------------------------------------
  return kernel

def test():
  '''This script will perform a unit test on your function, and provide useful
  output.
  '''

  np.set_printoptions(precision=3)

  ks =  [1, 2, 1, 2, 1]
  sds = [1, 2, 3, 4, 5]
  outputs = []
  # 1,1
  y = np.array([[ 0.075,  0.124,  0.075],
             [ 0.124,  0.204,  0.124],
             [ 0.075,  0.124,  0.075]])
  outputs.append(y)
  # 2,2
  y = np.array([[ 0.023,  0.034,  0.038,  0.034,  0.023],
             [ 0.034,  0.049,  0.056,  0.049,  0.034],
             [ 0.038,  0.056,  0.063,  0.056,  0.038],
             [ 0.034,  0.049,  0.056,  0.049,  0.034],
             [ 0.023,  0.034,  0.038,  0.034,  0.023]])
  outputs.append(y)
  # 1,3
  y = np.array([[ 0.107,  0.113,  0.107],
             [ 0.113,  0.120,  0.113],
             [ 0.107,  0.113,  0.107]])
  outputs.append(y)
  # 2,4
  y = np.array([[ 0.035,  0.039,  0.04 ,  0.039,  0.035],
             [ 0.039,  0.042,  0.044,  0.042,  0.039],
             [ 0.04 ,  0.044,  0.045,  0.044,  0.04 ],
             [ 0.039,  0.042,  0.044,  0.042,  0.039],
             [ 0.035,  0.039,  0.04 ,  0.039,  0.035]])
  outputs.append(y)
  # 1,5
  y = np.array([[ 0.11 ,  0.112,  0.11 ],
             [ 0.112,  0.114,  0.112],
             [ 0.11 ,  0.112,  0.11 ]])
  outputs.append(y)

  for k, sd, output in zip(ks, sds, outputs):
    if __name__ == "__main__":
      print "k:{}, sd:{}".format(k, sd)

    usr_out = make_gaussian(k, sd)

    if not type(usr_out) == type(output):
      if __name__ == "__main__":
        print "Error- output has type {}. Expected type is {}.".format(
            type(usr_out), type(output))
      return False

    if not usr_out.shape == output.shape:
      if __name__ == "__main__":
        print "Error- output has shape {}. Expected shape is {}.".format(
            usr_out.shape, output.shape)
      return False

    if not usr_out.dtype == output.dtype:
      if __name__ == "__main__":
        print "Error- output has dtype {}. Expected dtype is {}.".format(
            usr_out.dtype, output.dtype)
      return False

    if not np.all(np.abs(usr_out - output) < .005):
      if __name__ == "__main__":
        print "Error- output has value:\n{}\nExpected value:\n{}".format(
            usr_out, output)
      return False

    if __name__ == "__main__":
      print "Passed."

  if __name__ == "__main__":
    print "Success."
  return True

if __name__ == "__main__":
  # Testing code
  print "Performing unit test. Tests will be accepted if they are within .005 \
of the correct answer."
  test()
