import random

MIN_NUMBER_VALUE:int = 0
MAX_NUMBER_VALUE:int = 60
TRIPLETS_NUMBER:int = 20

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

# Generate a list of triplets
triplet_list = []
i = 0
while i < TRIPLETS_NUMBER:
    # Generate a valid triple
    a, b, c = generate_triplet(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)
    while validate_triplet(a, b, c) is False:
        a, b, c = generate_triplet(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)

    # Add up to the list
    triplet_list = triplet_list + [a, b, c]
    i = i + 1

# Title
print("# Number Speed and Accuracy\n")

# Print triplets
print("## Test\n")
i = 0
while i < TRIPLETS_NUMBER:
    print(f"{i+1:02d}: {triplet_list[i*3]:02d}   {triplet_list[i*3+1]:02d}   {triplet_list[i*3+2]:02d}\n>\n")
    i = i + 1

# Print furthers
print("## Solutions\n")
i = 0
while i < TRIPLETS_NUMBER:
    # Calculate further
    further = calculate_further_from_remaining(triplet_list[i*3], triplet_list[i*3+1], triplet_list[i*3+2])
    print(f"{i+1:02d}: {further:02d}")
    i = i + 1
