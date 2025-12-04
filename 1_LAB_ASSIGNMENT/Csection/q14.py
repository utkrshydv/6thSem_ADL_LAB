#name: "Utkarsh Yadav" roll: "23053172"
# Write a Python program to check substring existence.

def check_substring(string, substr):
    if substr in string:
        return True
    else:
        return False


string = input("Enter a string: ")
substr = input("Enter substr: ")
print(check_substring(string, substr))
