from typing import Any
import cv2 as cv
import dlib
import math
import numpy as np
image =cv.imread("jas.jpeg")
image1=cv.imread("jasprocess.jpg")
#img = cv.resize(img,(700,700))
print(image.shape[:])
DESIRED_HEIGHT = 1200
DESIRED_WIDTH = 600
def resize_and_show(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
  else:
    img = cv.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
  return img
def BlankCanvas(length, width):     # blank images maker with given inches 
	length=int(length*300)				# at 300 dpi 
	width=int(width*300)
	blank=np.zeros((length,width,3),dtype='uint8')    #8 bit to represent single pixel value 
	blank.fill(255)
	return blank
image=resize_and_show(image) 
image1=resize_and_show(image1)
canvas=BlankCanvas(12,8)
canvas=cv.imread("canvas.jpg")
startIndexX=200
startIndexY=150
canvas[startIndexX:image.shape[0]+startIndexX,startIndexY:image.shape[1]+startIndexY]=image1
xe=200
ye=startIndexY
x2=200
y2=image.shape[1]
canvas[startIndexX:image.shape[0]+startIndexX,image.shape[1]+startIndexY+x2:2*image.shape[1]+startIndexY+x2]=image
#canvas[image.shape[0]+startIndexX:]
print(canvas.shape[:])
cv.imwrite("image.jpg",canvas)
print(image.shape[:])
#cv.imshow("sexy",img)
cv.waitKey(0)
cv.destroyAllWindows()