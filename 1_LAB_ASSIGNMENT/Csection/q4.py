#name: "Utkarsh Yadav" roll: "23053172"
#count frequency of each character in a string

def count_freq(string):
  hashmap = {}
  for char in string:
    hashmap[char] = 1 + hashmap.get(char, 0)
  return hashmap

string = input("Enter a word: ")
print(count_freq(string))

for key, value in count_freq(string).items():
  print(f"{key} : {value}")