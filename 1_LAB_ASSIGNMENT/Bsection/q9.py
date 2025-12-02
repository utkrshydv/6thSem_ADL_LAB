#Find GCD of two numbers.
def findGCD(a, b):
  if b == 0:
    return a
  else:
    return findGCD(b, a%b)
  

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
print(findGCD(a,b))