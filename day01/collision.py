# -*- coding: utf-8 -*-
import random
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

x_min = 100;
y_min = 100;
x_max = 400;
y_max = 400;

rect1 = [random.randint(x_min,x_max),random.randint(y_min,y_max),random.randint(x_min,x_max),random.randint(y_min,y_max)]
rect2 = [random.randint(x_min,x_max),random.randint(y_min,y_max),random.randint(x_min,x_max),random.randint(y_min,y_max)]

print("rect1: %s, rect2: %s"%(rect1,rect2))
rect1_dx = (rect1[0]>rect1[2]) and rect1[0]-rect1[2] or rect1[2]-rect1[0]
rect1_dy = (rect1[1]>rect1[3]) and rect1[1]-rect1[3] or rect1[3]-rect1[1]
rect2_dx = (rect2[0]>rect2[2]) and rect2[0]-rect2[2] or rect2[2]-rect2[0]
rect2_dy = (rect2[1]>rect2[3]) and rect2[1]-rect2[3] or rect2[3]-rect2[1]

rect1_xmin = min(rect1[0],rect1[2])
rect1_ymin = min(rect1[1],rect1[3])
rect2_xmin = min(rect2[0],rect2[2])
rect2_ymin = min(rect2[1],rect2[3])

print(rect1_dx, rect1_dy, rect2_dx, rect2_dy)
print(rect1_xmin, rect1_ymin, rect2_xmin, rect2_ymin)

img = cv2.rectangle(img, (rect1[0], rect1[1]), (rect1[2], rect1[3]), (0,255,0), 1)
img = cv2.rectangle(img, (rect2[0], rect2[1]), (rect2[2], rect2[3]), (0,255,0), 1)

cv2.imshow('image', img)

if (rect1_xmin <= rect2_xmin and rect1_xmin+rect1_dx >= rect2_xmin and rect1_ymin <= rect2_ymin and rect1_ymin+rect2_dy >= rect2_ymin ):
    print("중첩")
else : print("non 중첩")
cv2.waitKey(0)
cv2.destroyAllWindows()