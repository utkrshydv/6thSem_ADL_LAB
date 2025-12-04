#name: "Utkarsh Yadav" roll: "23053172"
# Find the most frequent character in a string.

def most_freq(string):
    hashmap = {}

    for char in string:
        hashmap[char] = 1 + hashmap.get(char, 0)

    character = max(hashmap, key=hashmap.get)

    return [character, hashmap[character]]


string = input("Enter a string: ")
print(most_freq(string))
