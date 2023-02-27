# class Student:
#     name = 'Rohan'
#     age = 16
#
#
# s1 = Student()
# s2 = Student()
# print(s1.name, end='' )
# print(s2.name, end='')

# class Student:
#     pp = 50
#
# s1 = Student()
# s1.pp= 58
# s2 = Student()
# s2.pp = 60
# print(s1.pp)

# class Student:
#     name = 'Parikh'
#     def store_details(self):
#         self.age = 60
#     def print_details(self):
#         print(self.name, end='')
#         print(self.age)
# s = Student()
# s.store_details()
# s.print_details()

# class Student:
#     name = 'Parikh'
#     def store_details(self):
#         self.age = 60
#     def print_age(self):
#         print(self.age)
# s = Student()
# s.store_details()
# s1 = Student()
# s1.print_age()

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def print_student_details(self):
#         print(self.name, end= '')
#         print(self.age)
#
# s = Student('Rohan',60)
# s.print_student_details()

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_student_details():
#         print(self.name, end=" ")
#         print(self.age)
#
#     @staticmethod
#     def isTeen(age):
#         return age > 16
#
#
# a = Student.isTeen(18)
# print(a)


# class Student:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#
#
# def print_student_details():
#     print(self.__name, end= '')
#     print(self.age)
#
#
# s = Student('Rohan', 20)
# print(s.name)


# class Student:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#
#     def print_student_details(self):
#         print(self.__name, end= '')
#         print(self.age)
#
#
# s = Student('Rohan', 20)
# s.print_student_details()


# class Vehicle:
#     def __init__(self,color):
#         self.color = color
# class Car(Vehicle):
#     def __init__(self,color,numGears):
#         super().__init__(color)
#         self.numGears = numGears
# c= Car('black',5)
# print(c.color)

# class Vehicle:
#     def __init__(self,color):
#         self.color = color
#     def print(self):
#         print(self.color,end="")
# class Car(Vehicle):
#     def __init__(self,color,numGears):
#         super().__init__(color)
#         self.numGears = numGears
#     def print(self):
#        print(self.color,end="")
#        print(self.numGears)
# c = Car('black',5)
# c.print()


# class Circle(object):
#     def __str__(self):
#         return 'This is a Circle Class'
# c = Circle()
# print(c)


# class A:
#
#     def __init__(self):
#         print('init of A called')
# class B:
#     def __init__(self):
#         print('init of B called')
#
# class C(B,A):
#     def __init__(self):
#         super().__init__()
#
# c = C()


# class X:
#     pass
#
#
# class Y:
#     pass
#
#
# class Z:
#     pass
#
#
# class A(X, Y):
#     pass
#
#
# class B(Y, Z):
#     pass
#
#
# class C(B, A, Y):
#     pass

# class Vehicle:
#     def __init__(self, color):
#         self.__color = color
#
#
# class Car(Vehicle):
#     def __init__(self, color, numGears):
#         super().__init__(color)
#         self.numGears = numGears
#
#     def printCar(self):
#         print(c.__color, end=" ")
#         print(c.numGears)
#
#
# c = Car('black', 5)
# c.printCar()


# from abc import ABC,abstractmethod

# class A(ABC):
#
#     @abstractmethod
#     def fun1(self):
#         pass
#
#     @abstractmethod
#     def fun2(self):
#         pass
#
# class B(A):
#
#     def fun1(self):
#         print('function 1 called')
#
#     def fun2(self):
#         print('function 2 called')
# o = B()
# o.fun1()
#
# from abc import ABC,abstractmethod
#
# class A(ABC):
#
#     @abstractmethod
#     def fun1(self):
#         print('function of class A called')
#
#     @abstractmethod
#     def fun2(self):
#         pass
#
# class B(A):
#     def fun1(self):
#         print('function 1 called')
#     def fun2(self):
#         print('function 2 called')
# o = B()
# o.fun1()

# from abc import ABC,abstractmethod

# class A(ABC):
#
#     @abstractmethod
#     def fun1(self):
#         print('function of class A called')
#
#     @abstractmethod
#     def fun2(self):
#         pass
#
# class B(A):
#     def fun1(self):
#         super().fun1()
#     def fun2(self):
#         print('function 2 called')
# o = B()
# o.fun1()

# try:
#     a = 10
#     b = 0
#     c = a/b
#     print(c)
# except ValueError:
#     print('Exception occured')


# try:
#     a = 10
#     b = 0
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print('Exception occured')
#
# try:
#     a = 10
#     b = 0
#     c = a/b
#     print(c)
# except :
#     print('Exception occured')

# class ZeroDenominatorError(Exception):
#     pass
# try:
#     a = 10
#     b = 0
#     if(b==0):
#         raise ZeroDenominatorError()
#     c = a/b
# except ZeroDivisionError:
#     print('Zero Division Error occured')
#
# class ZeroDenominatorError(ZeroDivisionError):
#     pass
# try:
#     a = 10
#     b = 0
#     if(b==0):
#         raise ZeroDenominatorError()
#     c = a/b
# except ZeroDivisionError:
#     print('Zero Division Error occured')
# except ZeroDenominatorError:
#     print('Zero Denominator Error occured')

#
# class ZeroDenominatorError(ZeroDivisionError):
#     pass
# try:
#     a = 10
#     b = 0
#     if(b==0):
#         raise ZeroDenominatorError()
#     c = a/b
# except ZeroDivisionError:
#     print('Zero Division Error occured',end= '')
# except ZeroDenominatorError:
#     print('Zero Denominator Error occured',end = '')
# else:
#     print('else works')

# class ZeroDenominatorError(ZeroDivisionError):
#     pass
# try:
#     a = 10
#     b = 5
#     if(b==0):
#         raise ZeroDenominatorError()
#     c = a/b
# except ZeroDivisionError:
#     print('Zero Division Error occured',end= '')
# except ZeroDenominatorError:
#     print('Zero Denominator Error occured',end = '')
# else:
#     print('else works')



class ZeroDenominatorError(ZeroDivisionError):
    pass
try:
    a = 10
    b = 5
    if(b==0):
        raise ZeroDenominatorError()
    c = a/b
except ZeroDivisionError:
    print('Zero Division Error occured',end= '')
except ZeroDenominatorError:
    print('Zero Denominator Error occured',end = '')
else:
    print('else works',end='')
finally:
    print('finally works')
