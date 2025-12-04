#name: "Utkarsh Yadav" roll: "23053172"
#Count digits in a number

n = int(input("Enter a number: "))
count = 0
while n > 0:
  count = count + 1
  n = n//10

print(count)