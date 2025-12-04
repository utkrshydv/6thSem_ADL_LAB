#name: "Utkarsh Yadav" roll: "23053172"
#Write a program to check leap year

def checkLeap(year):
  if year % 400 == 0:
    print("Leap")
  elif year % 100 == 0:
    print("Not Leap")
  elif year % 4 == 0:
    print("Leap")
  else:
    print("Not Leap")

checkLeap(2025)
checkLeap(23053172)
checkLeap(2004)
  