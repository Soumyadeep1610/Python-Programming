#4. WAP to find all the numbers between 1000 and 3000 such that each digit of the number is the even number.


for number in range(1000, 3001):
    str_number = str(number)
    all_even = True
    for digit in str_number:   
        if int(digit) % 2 != 0:
            all_even = False
            break
    if all_even:
        print(number)
