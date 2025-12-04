#name: "Utkarsh Yadav" roll: "23053172"
#Write a program to reverse a number (e.g., 123 → 321).

num = 23053172

rem = num
rev = 0

while rem > 0:
  rev = rev*10 + rem%10
  rem = rem//10

print(f"{rev}")