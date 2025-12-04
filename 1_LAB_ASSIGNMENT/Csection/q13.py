#name: "Utkarsh Yadav" roll: "23053172"
# remove special characters from a string

def remove_special_char(string):
    sp_char = ['!', '@', '#', '$', '%', '^', '&', '*', '\'']
    new_string = ""
    for char in string:
        if char in sp_char:
            continue
        else:
            new_string += char
    return new_string


string = input("Enter a string: ")
print(remove_special_char(string))
