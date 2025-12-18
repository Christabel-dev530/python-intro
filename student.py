def name():
    print("Enter the name of student")
    name=input()
    return name

def studentclass():
    print("Enter class of student")
    studentclass=input()
    return studentclass

def amount():
    print("Enter the amount paid")
    amount=input()
    return amount

def total(name,studentclass,amount):
    print("This is", name, "she is in", studentclass, "she paid", amount)
total(name(),studentclass(),amount())

def number1():
    print("Enter number1")
    number1=float(input()) 
    return number1

def number2():
    print("Enter number2")
    number2=float(input())
    return number2

def number3():
    print("Enter number3")
    number3=float(input())
    return number3
def hurray():
    print("Hurray!, it is greater than 1000")
    
def ohno():
    print("oh no, it is less than 1000")    
    
def multiply(number1,number2,number3):
    multiply=number1*number2*number3
    print("The product is", multiply)
    if multiply>1000:
        hurray()
    else:
        ohno() 
multiply(number1(),number2(),number3())           
    
       
    
