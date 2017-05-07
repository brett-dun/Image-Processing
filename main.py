#!/usr/bin/env python

__author__ = "Brett Duncan"
__copyright__ = "Copyright 2017, Brett Duncan"
__credits__ = []
__license__ = ""
__version__ = "0.0.0"
__maintainer__ = "Brett Duncan"
__email__ = ""
__status__ = "Experimental"

from PIL import Image
import numpy as num

NUM_PHOTOS = 29

def main():
    
    im = Image.open('IMG_4300.jpg')
    print('IMG_4300.jpg');
    #images = [ num.array(im) ]
    
    sum = num.array(im)
    #print(sum)
    
    for i in range(1,NUM_PHOTOS):
        if i < 10:
            name = 'IMG_430' + str(i) + '.jpg'
        else:
            name = 'IMG_43' + str(i) + '.jpg'
        print(name)
        im = Image.open( name )
        sum += num.array(im);
        #print(sum);
            
    average = num.array(sum) / (NUM_PHOTOS)
    #print('Result')
    #print(average)
    im = Image.fromarray(average)
    im.save('test.jpg')
    print('DONE')

    """sum = num.array(im)
    
    for i in range(0,29):
        if i < 10:
            name = 'IMG_430' + str(i) + '.jpg'
        else:
            name = 'IMG_43' + str(i) + '.jpg'
        print(name)
        im = Image.open( name )
        imageArray = num.array(im)

        for j in range imageArray.shape[0]:
            for"""



if __name__ == '__main__':
    main();