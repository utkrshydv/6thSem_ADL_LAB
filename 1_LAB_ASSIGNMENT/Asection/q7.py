#name: "Utkarsh Yadav" roll: "23053172"
#Write a program to compute simple interest.

p, r, t = map(float, input("Enter Principal, Rate and Time(in years): ").split(", "))
print(f"Simple Interest: {(p*r*t)/100}")