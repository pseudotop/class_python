class Complex:
    def __init__(self, real=0, imag=0):
        self.__real = real
        self.__imag = imag

    def getReal(self):
        return self.__real

    def setReal(self, real):
        self.__real = real

    def getImag(self):
        return self.__imag

    def setImag(self, imag):
        self.__imag = imag

    def __str__(self):
        return '%d + %di'%(self.__real,self.__imag)

    def __add__(self, other):
        return Complex(self.__real+other.__real,\
                       self.__imag+other.__imag)

a = Complex(2,3)
b = Complex(3,1)
print(a)
print(b)
c = a + b
print(c)
