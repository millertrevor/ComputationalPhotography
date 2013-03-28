import sys
import os
import numpy as np
import cv2

def flipx(image):

  outputimage = None
  outputimage=image[::-1]
  return outputimage

def main():
  ''' This function applies your split script to images.

  It will search through the images/part0 subfolder, and apply your splitting 
  function to each one. It will then save the resulting images.
  '''
  imagesfolder0 = os.path.abspath(os.path.join(os.curdir, 'images', 'part0'))
  print '''Searching for images in {} folder
  (will ignore reversed in the name)'''.format(imagesfolder0)

  exts = ['.bmp', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.jpeg', '.jpg', 
    '.jpe', '.jp2', '.tiff', '.tif', '.png']

  for dirname, dirnames, filenames in os.walk(imagesfolder0):
    for filename in filenames:
      name, ext = os.path.splitext(filename)
      if ext in exts and 'reversed' not in name:
        print "Reversing image {}.".format(filename)

        img = cv2.imread(os.path.join(dirname, filename))
        reversedimage = flipx(img)
        cv2.imwrite(os.path.join(dirname,name+'reversed'+ext),reversedimage)
'''
        for values, color, channel in zip((red, green, blue), 
            ('red', 'green', 'blue'), (2,1,0)):
          img = np.zeros((values.shape[0], values.shape[1], 3), 
              dtype = values.dtype) 
          img[:,:,channel] = values
          print "Writing image {}.".format(name+color+ext)
          cv2.imwrite(os.path.join(dirname, name+color+ext), img)
          '''


def test():
  '''This script will perform a unit test on your function, and provide useful
  output.
  '''
  x = (np.random.rand(4,4,3) * 255).astype(np.uint8)

  if __name__ == "__main__":
    print "Input:\n{}".format(x)

  usr_reversed = flipx(x)

  true_reversed = x[::-1]
  

  for usr_out, true_out, name in zip((usr_reversed),
      (true_reversed), ('reversed')):

    if usr_out == None:
      if __name__ == "__main__":
        print "Error- {} has value None.".format(name)
      return False

    if not usr_out.shape == true_out.shape:
      if __name__ == "__main__":
        print "Error- {} has shape {}. Expected shape is {}.".format(name,
            usr_out.shape, true_out.shape)
      return False

    if not usr_out.dtype == true_out.dtype:
      if __name__ == "__main__":
        print "Error- {} has dtype {}. Expected dtype is {}.".format(name,
            usr_out.dtype, true_out.dtype)
      return False

    if not np.all(usr_out == true_out):
      if __name__ == "__main__":
        print "Error- {} has value:\n{}\nExpected value:\n{}".format(name,
            usr_out, true_out)
      return False

  if __name__ == "__main__":
    print "Success - all outputs correct."
  return True

if __name__ == "__main__":
  # Testing code
  print "Performing unit test."
  t = test()
  print "Unit test: {}".format(t)
  if t:
    main()
