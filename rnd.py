import random
rcp = ['가위','바위','보']
sel = input("(가위,바위,보) 중에서 하나를 선택하세요: ")
isel = 0;
if(sel == "가위"):
    isel = int(0)
elif(sel == "바위"):
    isel = int(1)
elif(sel == "보"):
    isel = int(2)
com = random.randint(0, 2)
print("사용자: %s 컴퓨터: %s"%(sel, rcp[com]))
if(sel is not rcp[com]):
    if(com == isel-1 or (isel==0 and com==2)):
        print("사람이 이겼음")
    elif(isel == com-1 or (isel==2 and com==0)):
        print("컴퓨터가 이겼음")
else:
    print("비김")
