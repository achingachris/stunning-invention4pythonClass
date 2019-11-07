def sum(a=10, b=15):
    add = a + b
    return add
print(sum())

def plus(a,b):
  sum = a + b
  return (sum, a)

# Call `plus()` and unpack variables 
sum, a = plus(3,4)

# Print `sum()`
print(sum)

def sum(a=10, b=15):
    a = 6
    b = 7
    add = a + b
    return add
print(sum())