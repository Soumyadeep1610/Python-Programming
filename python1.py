#1. Input a 4 digit number and print the even and odd digit and total even and odd digits.

number = input("Enter a 4-digit number: ")
even_digits = ''
odd_digits = ''
even_count = 0
odd_count = 0
for i in range(4):
    digit = number[i]  
    digit_int = int(digit)  
    if digit_int % 2 == 0:
        even_digits += digit 
        even_count += 1 
    else:
        odd_digits += digit 
        odd_count += 1  
print("Even digits:\n", even_digits)
print("Odd digits:\n", odd_digits)
print("Total even digits:", even_count)
print("Total odd digits:", odd_count) 
