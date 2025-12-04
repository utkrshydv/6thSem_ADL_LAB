#name: "Utkarsh Yadav" roll: "23053172"
# find lcm of two numbers
import math


def find_lcm(a, b):
    lcm = abs(a*b)//math.gcd(a, b)
    return lcm


def find_lcm_again(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print(find_lcm(a, b))
print(find_lcm_again(a, b))
