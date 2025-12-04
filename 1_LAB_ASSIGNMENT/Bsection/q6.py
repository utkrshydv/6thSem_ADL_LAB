#name: "Utkarsh Yadav" roll: "23053172"
#Check whether a number is a palindrome.

def checkPalindrome(number):
  rem = number
  rev = 0
  while rem > 0:
    rev = rev*10 + rem%10
    rem = rem//10
  
  if rev == number:
    return True
  else:
    return False
  
n = int(input("Enter a number: "))
print(checkPalindrome(n))