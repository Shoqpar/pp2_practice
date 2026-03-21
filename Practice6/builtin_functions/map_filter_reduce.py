# builtin_functions/map_filter_reduce.py

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# map()
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce()
total = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", total)

# Type checking
value1 = "123"
value2 = 45.6

print("\nType checking:")
print(value1, "is string?", isinstance(value1, str))
print(value2, "is integer?", isinstance(value2, int))
print(value2, "is float?", isinstance(value2, float))

converted_int = int(value1)
converted_str = str(value2)

print("\nType conversions:")
print("String to int:", converted_int)
print("Float to string:", converted_str)