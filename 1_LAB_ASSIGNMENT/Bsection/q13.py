#. Display sum of odd and even digits separately in a number.

n = int(input("Enter a number: "))

evenCount = 0
oddCount = 0

while n > 0: 
  num = n%10
  if num%2==0:
    evenCount = evenCount + num
  else:
    oddCount = oddCount + num
  n = n // 10

print(f"Odd Sum : {oddCount}, Even Sum: {evenCount}")
