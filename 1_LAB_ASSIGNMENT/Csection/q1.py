#name: "Utkarsh Yadav" roll: "23053172"
#Count number of vowels in a string

vowels = ["a", "e", "i", "o" ,"u"]

string = input("Enter a word: ")

count = 0

for ch in string:
  if ch.lower() in vowels:
    count += 1


print(f"Vowel Count: {count}")
