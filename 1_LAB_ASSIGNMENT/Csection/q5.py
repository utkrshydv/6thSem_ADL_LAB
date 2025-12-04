#name: "Utkarsh Yadav" roll: "23053172"
#convert string to uppercase without using built-in functions

def convert_upper(string):
  result = []
  for char in string:
    if 'a' <= char <='z':
      uppercase_char = chr(ord(char) - 32)
      result.append(uppercase_char)
    else:
      result.append(char)
  return "".join(result)

string = input("Enter a word: ")
print(convert_upper(string))