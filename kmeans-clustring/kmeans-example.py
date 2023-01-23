import numpy as np
import cv2 as cv
from matplotlib import pyplot as pt

x = np.random.randint(25,100,25)
y = np.random.randint(175,255,25)
z= np.hstack((x,y))
z = z.reshape((50,1))
z = np.float32(z)
'''
pt.hist(z,256,[0,256])
pt.show()
'''
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)


flags = cv.KMEANS_RANDOM_CENTERS

compactness, labels, centers = cv.kmeans(z,2,None,criteria, 10, flags)


A = z[labels==0]
B = z[labels==1]

pt.hist(A,256,[0,256],color='r')
pt.hist(B,256,[0,256],color='b')
pt.hist(centers, 32, [0,256],color='y')
pt.show()
