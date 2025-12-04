#name: "Utkarsh Yadav" roll: "23053172"
#Write a program to compute the remainder without using % operator.
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

# quotient = a // b
# remainder = a - b * quotient

# print(f"{remainder}")

while a > b:
  a = a-b

print(a)