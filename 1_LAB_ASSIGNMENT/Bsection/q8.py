#Generate Fibonacci series of N numbers.

a = 0
b = 1

n = int(input("Enter Number: "))

for i in range(n+1):
  print(a)
  c = a + b
  a = b
  b = c


