# method one:
print("---------------------------------------------------------------------")
print('take one: ')
print("---------------------------------------------------------------------")

x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y
print(('successfuly worked'))

# method 2
print("---------------------------------------------------------------------")
print('take two:')
print("---------------------------------------------------------------------")
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

print(('successfuly worked'))
