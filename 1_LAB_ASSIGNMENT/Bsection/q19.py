#name: "Utkarsh Yadav" roll: "23053172"
# Print the number of digits that are divisible by 3 in a given number.

n = int(input("Enter a number: "))

count = 0

while n > 0:
  num = n%10
  if num%3==0:
    count = count + 1
  n = n // 10

print("Number of digits divisible by 3: ", count)
