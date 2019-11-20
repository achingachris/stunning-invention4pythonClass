m = int(input('m: '))
n = int(input('n: '))

def multiple(m, n):
  return True if m % n == 0 else False

print(multiple(m, n))

# method 2
print("###### mtehd 2 #######")
int1 = int(input('Enter interger 1: '))
int2 = int(input('Enter interger 2: '))


def multiple(m, n):
	return True if m % n == 0 else False

print(multiple(int1, int2))
# print(multiple(7, 2))