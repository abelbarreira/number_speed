import random

MIN_NUMBER_VALUE:int = 0
MAX_NUMBER_VALUE:int = 80

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def calculate_diff(a, b):
    if a >= b:
        return a-b
    else:
        return b-a

def generate_triplet(min_value, max_value):
    # Get a
    a = generate_random_number(min_value, max_value)

    # Get b different to a
    b = generate_random_number(min_value, max_value)
    while a == b:
      b = generate_random_number(min_value, max_value)

    # Get c different to a and to b
    c = generate_random_number(min_value, max_value)
    while (c == a) or (c == b):
      c = generate_random_number(min_value, max_value)

    return a, b, c

def get_lowest(a, b, c):
   if (a < b) and (a < c):
        return a
   if (b < a) and (b < c):
        return b
   if (c < a) and (c < b):
        return c

def get_highest(a, b, c):
   if (a > b) and (a > c):
        return a
   if (b > a) and (b > c):
        return b
   if (c > a) and (c > b):
        return c

def get_remaining(a, b, c):
   lowest = get_lowest(a, b, c)
   highest = get_highest(a, b, c)

   if (a == lowest) or (a == highest):
       if (b == lowest) or (b == highest):
           return c
       if (c == lowest) or (c == highest):
           return b
   else:
       return a

def validate_triplet(a, b, c):
    lowest = get_lowest(a, b, c)
    highest = get_highest(a, b, c)
    remaining = get_remaining(a, b, c)

    diff_r_l = calculate_diff(remaining, lowest)
    diff_r_h = calculate_diff(highest, remaining)

    if diff_r_l != diff_r_h:
        return True

    return False

def calculate_further_from_remaining(a, b, c):
    lowest = get_lowest(a, b, c)
    highest = get_highest(a, b, c)
    remaining = get_remaining(a, b, c)

    diff_r_l = calculate_diff(remaining, lowest)
    diff_r_h = calculate_diff(highest, remaining)

    if diff_r_l > diff_r_h:
        return lowest
    else:
        return highest

# Generate a new valid triplet
a, b, c = generate_triplet(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)
while validate_triplet(a, b, c) is False:
    a, b, c = generate_triplet(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)

print(f"a: {a}, b: {b}, c: {c}")

lowest = get_lowest(a, b, c)
print(f"lowest: {lowest}")

highest = get_highest(a, b, c)
print(f"highest: {highest}")

remaining = get_remaining(a, b, c)
print(f"remaining: {remaining}")

further = calculate_further_from_remaining(a, b, c)
print(f"further: {further}")