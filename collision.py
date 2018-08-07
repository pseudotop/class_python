import random

x_min = 0;
y_min = 0;
x_max = 10;
y_max = 10;

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

if (rect1_xmin <= rect2_xmin and rect1_xmin+rect1_dx >= rect2_xmin and rect1_ymin <= rect2_ymin and rect1_ymin+rect2_dy >= rect2_ymin ):
    print("중첩")
else : print("non 중첩")
