class Student:
    def go_to_school(self):
        self.name = '홍길동'
        print(self.name,'은 학교에 갑니다')
    def do_studying(self):
        print(self.name,'은 공부를 합니다')
        print(dir(self))

s = Student()
s.go_to_school()
s.do_studying()

print(dir(s))