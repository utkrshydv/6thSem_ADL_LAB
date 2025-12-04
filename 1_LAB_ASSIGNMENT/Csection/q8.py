#name: "Utkarsh Yadav" roll: "23053172"
# replace all vowels with '*'

def check_vowel(string):
    vowels = ["a", "e", "i", "o", "u"]
    if string.lower() in vowels:
        return True
    else:
        return False


def replace_vowels(string):
    new_string = ""
    for char in string:
        if check_vowel(char):
          new_string += "*"
        else:
          new_string += char
    return new_string


string = input("enter a word: ")
print(replace_vowels(string))
