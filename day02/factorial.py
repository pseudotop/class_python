import time
fact = 1
n = int(input("팩토리얼 n값: "))
tic,toc = 0,0
for i in range(1,n+1):
    fact *= i
    if(i%100000==0):
        toc = time.clock()
        runningtime = toc-tic
        tic = time.clock()
        print("중간값:",i, "소요시간:",runningtime)

print(n,"!은",fact,"이다")
order = 0
for j in str(fact):
    order += 1
print("자릿수: ", order)