import sys
from PIL import Image
import numpy as np


def main():
    
    print('STARTING')
    
    scaler_n = int(sys.argv[1]) #Scaler numerator (positive integer, larger value increases brightness)
    scaler_d = int(sys.argv[2]) #Scaler denominator  (positive integer, larger value decreases brightness)
    colors = int(sys.argv[3]) #Number of colors
    file_paths = sys.argv[4:] #Read in the file names
    
    sum = np.array( Image.open( file_paths[0] ) ) #Create the list
    sum = 0 #Set the list equal to zero
    
    count = 0
    for p in file_paths: #For each file
        
        print(p) #print the file to let us know which file is being processed
        im = Image.open( p ) #Open the image
        imageArray = np.array( im ) #Save the image as an array
        
        imageArray = (imageArray / (255/colors)) * (255/colors) #Save the array with a preset number of colors
        
        sum += imageArray #Add this to the sum
        count += 1 #Increment the count
            
    average = np.array(sum) / count * scaler_n / scaler_d #Find the average and process the image using the scalers
    
    output = Image.fromarray(average) #Store the array to an image
    output.save('test.jpg') #Write the image to a file
    print('DONE')


if __name__ == '__main__':
    main()