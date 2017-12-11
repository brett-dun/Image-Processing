#!/usr/bin/env python

import sys
from PIL import Image
import numpy as np

def main():
    
    print('STARTING')

    init = np.array( Image.open( sys.argv[1] ) )
    output = init

    numColors = 16 #64 max

    for i in range(1,len(init)-1):
    	for j in range(1, len(init[0])-1):
    		for k in range(0, len(init[0][0])):
    			output[i][j][k] = ( init[i-1][j][k] / 4 + init[i][j-1][k] / 4 + init[i+1][j][k] / 4 + init[i][j+1][k] / 4 ) / (64/numColors) * (64/numColors)
    	txt = str(i) + ' of ' + str(len(init)-1) + ' complete'
    	print(txt)

    im = Image.fromarray(output) #Store the array to an image
    im.save('reducedNoise.jpg') #Write the image to a file
    print('Noise Reduction Complete')


if __name__ == "__main__":
    main();