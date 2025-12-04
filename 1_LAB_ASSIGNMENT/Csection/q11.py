#name: "Utkarsh Yadav" roll: "23053172"
# Convert string to title case manually.

def title_case(string):
  words = string.split()
  new_words = []
  for word in words:
    new_word = word[0].upper() + word[1:].lower()
    new_words.append(new_word)

  return " ".join(new_words)

string = input("Enter a string: ")
print(title_case(string))
