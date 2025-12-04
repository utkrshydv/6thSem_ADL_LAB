#name: "Utkarsh Yadav" roll: "23053172"
#Count number of prime numbers in a range.
def checkPrime(num):
  if num < 2:
    return
  
  factorCount = 0
  
  for i in range(1, num//2+1):
    if num%i == 0:
      factorCount = factorCount + 1
  
  if factorCount == 1:
    return True
  

n = int(input("Enter a range: "))
count = 0
for i in range(n+1):
  if checkPrime(i):
    count = count + 1

print(count)