#name: "Utkarsh Yadav" roll: "23053172"
# extract all the digit in a string

import re #regular expression

def extract_digits(string):
    result = []
    for char in string:
        if not char.isalpha():
            result.append(char)

    return result

def extract_digits_re(string):
    for char in string:
        if not re.match(r"[A-Za-z]", char):
          print(char)


string = input("Enter a string: ")
print(extract_digits(string))
extract_digits_re(string)
