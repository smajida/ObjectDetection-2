import utils
import input_data as id
import numpy
import cv2
import time

IMAGE_SIZE = 64

# test image load / show
image = utils.getImage('../space_crater_dataset/images/tile1_24.pgm')
#utils.showImage('full image', image)
#print image
#print utils.getSubImage(image, 100, 100, (6,6))

#test sub image
#utils.showImage('sub image', utils.getSubImage(image, 500, 500, (100, 200)))

#test resizing image
#utils.showImage('resize image', utils.scaleImage(image, (500, 500)))

#test sliding window
#for window in utils.slidingWindow(image, 100, (100,100)):
#    utils.showImage('window', window)

# test input_data.Data class
data = id.Data(IMAGE_SIZE, IMAGE_SIZE)
data.add('../space_crater_dataset/data/1_24.csv','../space_crater_dataset/images/tile1_24.pgm')
data.finalize()

src = utils.getImage('../space_crater_dataset/images/tile1_24.pgm')

for i in range(data.num_examples):
    img = data.images[i]
    label = data.labels[i]
    coords = data.coords[i]
    x = coords[0]
    y = coords[1]
    r = coords[2]
    
    
    if label[1] == 1:
        cv2.circle(src,(x,y), r/2, (0,0,255), 0)
        
utils.showImage('craters', utils.scaleImage(src, (1000,1000)))
