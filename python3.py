#3. Input a 10 digit number and print the alternate digits.

number = input("Enter a 10-digit number: ")
i = 0
while i < 10:
    print(number[i], end=" ")
    i += 2