#!/usr/bin/env python

import sys
from PIL import Image
import numpy as np
from scipy import ndimage

'''
Warning: this code is horribly slow, implement the following solution: 
https://gis.stackexchange.com/questions/254753/calculate-the-average-of-neighbor-pixels-for-raster-edge
'''
def main():
    
    print('STARTING')

    #create numpy array from input image
    init = np.array(Image.open(sys.argv[1]))

    #split
    channel0 = init[:,:,0]
    channel1 = init[:,:,1]
    channel2 = init[:,:,2]

    output0 = ndimage.generic_filter(input=channel0, function=np.nanmean, size=3, mode='constant', cval=np.NaN)
    print('channel0 complete')
    output1 = ndimage.generic_filter(input=channel1, function=np.nanmean, size=3, mode='constant', cval=np.NaN)
    print('channel1 complete')
    output2 = ndimage.generic_filter(input=channel2, function=np.nanmean, size=3, mode='constant', cval=np.NaN)
    print('channel2 complete')

    #create output numpy array full of zeros
    output = np.dstack((output0, output1, output2))

    #number of allowable color variation per color channel - max is 64
    #num_colors = 16

    #iterate through the array
    '''
    for i in range(1,len(init)-1):
    	for j in range(1, len(init[i])-1):
    		for k in range(0, 3):
                #average the four neighboring pixels
    			output[i][j][k] = ( init[i-1][j][k] / 4 + init[i][j-1][k] / 4 + init[i+1][j][k] / 4 + init[i][j+1][k] / 4 ) / (64/num_colors) * (64/num_colors)
    	txt = str(i) + ' of ' + str(len(init)-1) + ' complete'
    	print(txt)
    '''

    #convert from numpy array to PIL image
    im = Image.fromarray(output)

    #save the image to a file
    im.save('reducedNoise.jpg')

    print('Noise Reduction Complete')


if __name__ == "__main__":
    main()
