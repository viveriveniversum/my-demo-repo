number = int(input("Number to check: "))
# we need the length of number
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

# viveriveniversum @ github ------C7208-Onur MANAP
