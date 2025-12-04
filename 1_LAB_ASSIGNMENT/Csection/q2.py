#name: "Utkarsh Yadav" roll: "23053172"
#reverse a string without slicing

def rev_string(s):
  reversed = ""
  for char in s:
    reversed = char + reversed
  return reversed

string = input("Enter a word: ")
print(rev_string(string))