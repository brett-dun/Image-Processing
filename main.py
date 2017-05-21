#!/usr/bin/env python


__author__ = "Brett Duncan"
__copyright__ = "Copyright 2017, Brett Duncan"
__credits__ = []
__license__ = ""
__version__ = "0.0.0"
__maintainer__ = "Brett Duncan"
__email__ = ""
__status__ = "Experimental"


import sys
from PIL import Image
import numpy as num


SCALER_N = 1 #Numerator of the scaler
SCALER_D = 1 #Denomoninator of the scaler
COLORS = 255 #Number of colors


def main():
    
    print('STARTING')
    file_paths = sys.argv[1:] #Read in the file names
    
    sum = num.array( Image.open( file_paths[0] ) ) #Create the list
    sum -= num.array( Image.open( file_paths[0] ) ) #Set the list's values to zero
    
    count = 0
    for p in file_paths: #For each file
        
        #print(p)
        im = Image.open( p ) #Open the image
        imageArray = num.array( im ) #Save the image as an array
        
        imageArray = (imageArray / (255/COLORS)) * (255/COLORS) #Save the array with a preset number of colors
        
        sum += imageArray #Add this to the sum
        count += 1 #Increment the count
            
        average = num.array(sum) / count * SCALER_N / SCALER_D #Find the average and process the image using the scalers
    
    im = Image.fromarray(average) #Store the array to an image
    im.save('test.jpg') #Write the image to a file
    print('DONE')


if __name__ == '__main__':
    main();