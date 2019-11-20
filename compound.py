# Import math module for 'Pow' function
import math

# Take input from user (Principal, rate, time)
principal = float (input("Enter principal : "))
rate = float (input("\nEnter rate : "))
time = float(input("\nEnter time (year) : "));    

# Calculate compound interest 
result = principal * math.pow((1 + rate / 100), time)

'''
The pow(x, y) is equivalent to: x**y
'''

# Print the result
print("\nCompound interest :", result)

# another method
print('take to::::::::::::::')

p = float(input('Please enter principal amount:'))
t = float(input('Please enter number of years:'))
r = float(input('Please enter rate of interest:'))
n = float(input('Please enter number of times the interest is compounded in a year:'))
a = p*(1+(r/(100*n))**(n*t))
print('Amount compounded to: ', a)