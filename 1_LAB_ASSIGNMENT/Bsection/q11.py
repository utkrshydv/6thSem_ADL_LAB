#Print all prime numbers between 1 and 100.
def checkPrime(num):
  if num < 2:
    return 
  
  factorCount = 0
  
  for i in range(1, num//2+1):
    if num%i == 0:
      factorCount = factorCount+1

  if factorCount == 1:
    print(num)


for i in range(101):
  checkPrime(i)