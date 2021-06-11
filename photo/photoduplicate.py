import numpy as np
import cv2 as cv


img1 = cv.imread('Path1')
img1 = cv.resize(img1, (200, 200))
array1 = np.asarray(img1)

img2 = cv.imread('Path2')
img2 = cv.resize(img2, (200, 200))
array2 = np.asarray(img2)

class BreakIt(Exception) : pass

flag = 0

try:
    for i, j in zip(array1, array2):
        for a, b in zip(i, j):
            for x, y in zip(a, b):
                if x != y:
                    flag = 1
                    print("Not a duplicate")
                    raise BreakIt
except:
    pass

if flag == 0:
    print("Duplicate")
