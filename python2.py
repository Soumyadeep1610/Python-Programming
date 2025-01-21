#2. Input a 10 digit number and find the digit which is maximum.


number = input("Enter a 10-digit number: ")
digit_count = [0] * 10
for digit in number:
    digit_int = int(digit)  
    digit_count[digit_int] += 1  
max_count = 0
max_digit = None
for i in range(10):
    if digit_count[i] > max_count:
        max_count = digit_count[i]
        max_digit = i
print(f"The digit that appears the most is: {max_digit} (appears {max_count} times)")