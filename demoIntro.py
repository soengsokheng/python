#x = "awesome"
#def myfunc():
    #x = "amazing"
    #print("Python is " + x)
#myfunc()
#print("python is "+ x)

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)
#print(result)
#x = 5
#y = x
#print(type(x))
#print(id(x)) 
#print(id(y))
x= 500
print(id(x))

x=y=z=50
print("The value of x is",x)
print("The value of y is",y)
print("The value of z is",z)

#name = input("Name : ")
#age = input("Age : ")
#batch = input("Batch : ")
#dep = input("Department : ")

#print("-Name : ",name)
#print("-Age : ",age)
#print("-",batch)
#print("-",dep)

#import time
#for seconds in range(10,0,-1):
    #print(seconds)
    #time.sleep(1)
#print("Happy NewYear!!")

#rows = int(input("Enter rows: "))
#coloums = int(input("Enter coloums: "))
#symbol = input("Enter a symbol that you want to use: ")
#for i in range(rows):
    #for j in range(coloums):
       # print(symbol, end="")
  # print()
    

num1 = 6
num2 = 4
print("The addition of two numbers is",num1+num2)
print("The subtraction of two numbers is",num1-num2)
print("The multiplication of two numbers is",num1*num2)
print("The division of two numbers is",num1/num2)
#list
# 1.The list is a sequence data type which is used to store the collection of data
# 2.list is a collection of things, enclosed in [ ] and seperated by commas.
lang = ["C Programming", "C++", "Python"]
ide = ["Dev C++", "VS Code", "Pycharm"]
print(type(lang), type(ide))
print(lang[1])
print(ide)
#Nested Lists
fruits_name = [['lemon','orange'],['apple','mango']]
print(fruits_name[1])
'''Negative Indexing'''
print(fruits_name[1])

fruits = input("Enter some string : ")
print(fruits.split())