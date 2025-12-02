#Count even and odd numbers in a list.
mylist = [0, 1, 2, 3, 4, 5, 6, 7]
odd = 0
even = 0

for i in mylist:
  if i%2==0:
    even = even + 1
  else:
    odd = odd + 1

print(f"odd: {odd}, even: {even}")