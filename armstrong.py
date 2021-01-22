number = int(input("Number to check: "))

l = len(str(number))
total = 0

a = number
while a > 0:
    digit = a % 10
    total += digit**l
    a //= 10

if number == total:
    print(number, "is an Armstrong number!")
else:
    print(number, "is not an Armstrong number!")
