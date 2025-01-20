2.1/1!+2/2!+3/3!+…………+n/n!

import math

def series_sum(n):
    total_sum = 0  # Initialize the sum to 0
    for i in range(1, n + 1):
        total_sum += i / math.factorial(i)  # Add the term i / i!
    return total_sum

# Example: Compute the sum for n = 5
n = 5
result = series_sum(n)
print(f"The sum of the series for n={n} is: {result}")
