#name: "Utkarsh Yadav" roll: "23053172"
#Write a program to calculate compound interest.
p, r = map(float, input("Enter Principal and interest: ").split(", "))
n, t = map(int, input("Enter number of times and years: ").split(", "))

compoundInterest = (p*((1 + (r/n))**(n*t)))-p
print(f"Compound Interest: {compoundInterest:.2f}")