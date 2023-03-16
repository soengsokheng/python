#Calculate the square of number
num = int(input("Enter the number: "))
print("The square of number is: ",num**2)
print("-----------------------------------")

#Convert Fahrenheit into Celsius
fahrenheit = float(input("Enter the value of Fahrenheit: "))
celsius = (((fahrenheit-32)*5)/9)
print("The value of Celsius is: ",celsius)
print("-----------------------------------")

#Simple Interest and Compound Interest
#Simple Interest
principal_amount = float(input("Enter principal Amount: "))
time = float(input("Enter the time: "))
rate = float(input("Enter the rate: "))
simple_interest = (principal_amount*time*rate)/100
print("The Simple Interest is: ",simple_interest)
#Compound Interest
principal_a = float(input("Enter the principal amount: "))
rate2 = float(input("Ente rate of interest: "))
time2 = float(input("Enter time: "))
amount = principal_a*(1+(rate/100))**time2
compound_interest = amount  - principal_a
print("The Compound Interest is: ",compound_interest)
print("------------------------------------")

#Sum of all elements in the list
list = [11,6,43,1,8]
total = sum(list)
print("Sum of all elements is: ",total)
print("------------------------------------")

#Find area and perimeter of a square
side = float(input("Enter the value of side: "))
area = side**2
perimeter = side**4
print("The area of square is: ",area)
print("The perimeter of square is: ",perimeter)