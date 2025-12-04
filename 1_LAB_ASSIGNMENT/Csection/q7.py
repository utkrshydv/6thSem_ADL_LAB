#name: "Utkarsh Yadav" roll: "23053172"
#count words in a string

def count_words(string):
  return len(string.split())

string = input("Enter a string: ")
print(count_words(string))