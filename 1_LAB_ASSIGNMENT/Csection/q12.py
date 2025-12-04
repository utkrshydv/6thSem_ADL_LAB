#name: "Utkarsh Yadav" roll: "23053172"
# check if two strings are anagrams

def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    hashmap1 = {}
    hashmap2 = {}

    for char in str1:
        hashmap1[char] = 1 + hashmap1.get(char, 0)

    for char in str2:
        hashmap2[char] = 1 + hashmap2.get(char, 0)

    return hashmap1 == hashmap2


str1 = input("Enter 1st word: ")
str2 = input("Enter 2nd word: ")
print(check_anagram(str1, str2))
