#name: "Utkarsh Yadav" roll: "23053172"
#remove all spaces from a string

def remove_space(string):
  return "".join(string.split())

string = input("Enter a string: ")
print(remove_space(string))