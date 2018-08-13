class Counter:
    def __init__(self):
        # count --> __count면 namespace에 '_Counter__count'로 변형돼서 저장
        # 이는 private class와 비슷하지만 결국에 사용 가능
        self.__count = 0
    def reset(self):
        self.__count = 0
    def increment(self):
        self.__count += 1
    def get(self):
        return self.__count

c = Counter()
#c.reset()

for i in range(10):
    c.increment()
print(c.get())
print(dir(c))