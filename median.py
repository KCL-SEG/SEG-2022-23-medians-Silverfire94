"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
middle = len(numbers) / 2
median = 0
if len(numbers)%2 == 1:
    median = numbers[round(middle)]
else:
    median = (numbers[int(middle)] + numbers[int(middle - 1)]) / 2

print(median)
