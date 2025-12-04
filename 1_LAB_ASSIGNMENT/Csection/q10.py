#name: "Utkarsh Yadav" roll: "23053172"
# find longest word from a sentence

def find_longest_word(string):
    result = string.split()
    longest_word = max(result, key=len)
    return longest_word


string = input("Enter a word: ")
print(find_longest_word(string))
