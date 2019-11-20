# Define a function to convert
# celsius temperature to Fahrenheit
def Celsius_to_Fahrenheit(c) :
    
    f = (9/5)*c + 32
    
    return f
    
# Define a function to convert
# Fahrenheit temperature to Celsius
def Fahrenheit_to_Celsius(f) :
    
    c = (5/9)*(f - 32)
    
    return c
    

# Driver Code
if __name__ == "__main__" :
    
    c = 60
    print(c, "degree celsius is equal to:",Celsius_to_Fahrenheit(c),"Fahrenheit")
    
    f = 45
    print(f,"Fahrenheit is equal to:",Fahrenheit_to_Celsius(f),"degree celsius")

    # other methd
    print((''))
    print('::::::method 2:::::::')
temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")