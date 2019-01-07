
import sys
from PIL import Image
import numpy as np

def main():
    
    print('STARTING')

    #read in file names from command line
    file_paths = sys.argv[1:]

    #open the image
    im = Image.open(file_paths[0])
    #get image sizing information
    width, height = im.size
    
    #array to hold 
    array = np.zeros((height, width, 3), dtype=np.uint8)
    #array2 = np.zeros((height, width, 3), dtype=np.int64)
    
    #count = 0
    for p in file_paths: #For each file
        
        #print the file to let us know which file is being processed
        print(p)

        #open the image
        im = Image.open(p)

        #convert the image to a numpy array
        im_array = np.array(im, dtype=np.uint8)

        #take the maximum of the pixel values between the cumulative array and the image array
        array = np.maximum(array, im_array)

        #array2 = np.minimum(array2, im_array)
        #array2 += im_array.astype(np.int64)

        #count += 1 #Increment the count

    #array2 = array2 / count

    #color channels with a value less than 32
    threshold_indexes = array < 32
    #set them to 0
    array[threshold_indexes] = 0

    #this will brighten the pixels that are not below the threshold
    #changes range from [0, np.max(array)] to [0, 255]
    array = (array / np.max(array) * 255).astype(np.uint8)

    #this makes the stars a lot brighter but also makes coloring and brightness less realistic
    '''threshold_indexes = array >= 32
    array[threshold_indexes] = 255'''

    '''
    threshold_indexes = array2 < 8
    array2[threshold_indexes] = 0

    threshold_indexes = array2 >= 8
    array2[threshold_indexes] = 255
    '''

    #convert from numpy array to PIL image
    output = Image.fromarray(array)
    #save image as a file
    output.save('test.jpg')

    #output = Image.fromarray(array2.astype(np.uint8))
    #output.save('test2.jpg')

    print('DONE')


if __name__ == '__main__':
    main()
