#name: "Utkarsh Yadav" roll: "23053172"
# Check whether a number is Armstrong.

def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count


def check_armstrong(num):
    dup_num = num
    sum_ = 0

    count = count_digits(num)

    while dup_num > 0:
        temp = dup_num%10
        sum_ = sum_ + temp**count
        dup_num = dup_num //10
      
    return sum_ == num



n = int(input("Enter a number: "))
print(check_armstrong(n))

print(count_digits(123))
print(len(str(123)))
check_armstrong(123)
