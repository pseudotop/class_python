import math

def sphereVolume(r):
    return 4/3*math.pi*(r**3)

radius = float(input("구의 반지름: "))
print("구의 부피: ",sphereVolume(radius))