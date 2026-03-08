# Factorial of a number
# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("Factorial of",n,"is",fact)

# Function

# def avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(f"{avg:.2f}")
#     return avg
# avg(5,11,15)

# len of the list 
# list1=[1,2,3,4,5]
# list2=[1,2,3,4,5,6,7,8,9]
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
# print_list(list1)
# print()

# calculate factorial using function
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# n=int(input("Enter a number: "))
# print(f"Factorial of {n} is {factorial(n)}")

# convert usd to inr using function
# def usd_to_inr(usd):
#     inr=usd*82.5
#     print(inr)
#     return inr 
# usd_to_inr(100)

# if odd then print odd else print even
# def odd_even(n):
#     if n%2==0:
#       return "Even"
#     else:
#       return "Odd"
# n=int(input("Enter a number: "))
# print(odd_even(n))

# Recursion 
# def show(n):
#     if n == 0:
#         return
#     print(n)
    
#     show(n-1)
# show(5)

# recusrion of factorial
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(4))

# def fact(n):
#     if n==0:
#         return 1
#     return fact(n-1)*n
# print(fact(5))

# write a program a recursive function to calculate the sum of first n numbers
# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n-1)
# print(sum(5))


# def print_list(list,idx=0):
#     if idx == len(list):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# list=[1,2,3,4,5] 
# print_list(list)

##File I/O
# file=open("sample_file.txt","a")
# file.write("Hello sir,  this is a sample file Bhushan.\n")
# file.close()

# with open("sample_file.txt","r") as file:
#     content=file.read()
#     print(content)

# with open("sample_file.txt","w") as file:
#     a=file.write("Hello sir,  this is a sample file.\n")
#     print(a)

# replace the content of the file
# with open("sample_file.txt","r") as file:
#     data=file.read()
# new_data=data.replace("Hello","Hi")
# with open("sample_file.txt","w") as file:
#     file.write(new_data)


# # Python OOP
# class-blueprint for creating objects
# object-instance of a class

# class student:   #class
#     name="Bhushan"
# s1=student()     #object
# print(s1.name)

# class car:
#     name="BMW"
#     color="Black"
#     price=50000000
# c1=car()
# print(c1.name)
# print(c1.color)
# print(c1.price)

# Constructor definition - All classes have a constructor by default
# which is used to initialize the object. 
# It is defined using __init__ method.
# automatically called when an object is created.

# class student:
#     def __init__(self):  #Default constructor
#         pass
#     def __init__(self,name,age,roll_no):  #Parametrized constructor
#         self.name=name
#         self.age=age
#         self.roll_no=roll_no
#         print("Constructor called")
# s1=student("Bhushan",22,51)
# print(s1.name)
# print(s1.age)
# print(s1.roll_no)

# Decorators- A decorator is a function that takes
# another function and extends its behavior without 
# explicitly modifying it.
# static method- A static method is a method that belongs
# to a class rather than an instance of the class.
# It does not require access to instance-specific
# data and can be called on the class itself.

# oop -object oriented programming
# Abstraction- Hiding the internal details and showing only the functionality to the user.
# Encapsulation- Wrapping the data and methods that operate on the data into a single unit called a class.
# Inheritance- The ability of a new class to inherit properties and behaviors from an existing class.     
# Polymorphism- The ability of different classes to be treated as instances of the same class through a common interface.
#               It allows methods to do different things based on the object it is acting upon.


# class Account:
#     def __init__(self,balance,acc):
#         self.balance=balance
#         self.acc=acc
#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs,",amount,"debited from account")
#         print("Current balance:",self.balance)
#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs.",amount,"credited to account")
#         print("Current balance:",self.balance)
# acc1=Account(10000,"Savings")
# acc1.debit(2000)
# acc1.credit(5000)
# acc1.debit(1000)

# Inheritance and static method
# class car:
#     @staticmethod
#     def start():
#         print("Car started")
#     @staticmethod
#     def stop():
#         print("Car stopped")

# class Tata(car):
#     def __init__(self,name,color,price):
#         self.name=name
#         self.color=color
#         self.price=price
#     def display(self):
#         print("Name:",self.name)
#         print("Color:",self.color)
#         print("Price:",self.price)

# car1=Tata("Tata Nexon","Red",1000000)
# car2=Tata("Tata Altroz","Blue",800000)
# print(car1.start())
# print(car1.stop())
# print(car1.display())


# class method:- A method is a function that is defined 
# within a class and is associated with an object of that class.
# It can access and modify the attributes of the object and 
# perform specific actions related to the class. 
# Methods are called on objects and can take parameters to 
# perform operations on the object's data.

# property decorator- The @property decorator in Python is 
# used to define a method as a property. 
# It allows you to access the method like an attribute, 
# without explicitly calling it as a method.

# Complex number class with operator overloading
# class complex():
#     def __init__(self,real,imag):
#         self.real=real
#         self.imag=imag
#     def display(self):
#        print (self.real,"i +",self.imag,"j")
#     def __sub__(c1,c2):
#         diff_real=c1.real-c2.real
#         diff_imag=c1.imag-c2.imag
#         return complex(diff_real,diff_imag)

# c2=complex(2,3)
# c1=complex(4,5)
# c1.display()
# c2.display()
# num3=c1-c2
# num3.display()

# Circle class with area and circumference
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return (22/7)*self.radius**2
#     def circumference(self):
#         return 2*(22/7)*self.radius
# c1=circle(2)
# print("Area of circle:",c1.area())
# print("Circumference of circle:",c1.circumference())

# What is virtual environment?
# Isolated Python environment for managing dependencies.
# Command:
# python -m venv venv

