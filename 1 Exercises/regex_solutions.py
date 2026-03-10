import re

# R-numbers
def check_r_numbers(id_list):
    # starts with R/r, followed by 7 numbers, first is 0 or 1
    pattern = re.compile(r'^[Rr][01]\d{6}$')
    valid = []
    invalid = []
    for item in id_list:
        if pattern.match(item):
            valid.append(item)
        else:
            invalid.append(item)
    return valid, invalid

# Numbers in text (1-3 digits)
def find_numbers_1_to_3(text):
    # Match numbers 1-3 digits long, ensure they aren't part of longer numbers using word boundaries
    return re.findall(r'\b\d{1,3}\b', text)

# Casing converter
def pascal_to_snake(text):
    # Convert PascalCase to snake_case
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_to_pascal(text):
    # Convert snake_case to PascalCase
    return "".join(x.capitalize() for x in text.split("_"))

def detect_and_convert_casing(text):
    if "_" in text:
        return snake_to_pascal(text)
    else:
        return pascal_to_snake(text)

# Whitespace removal
def remove_extra_whitespaces(text):
    return re.sub(r'\s+', ' ', text).strip()

# Split with multiple delimiters
def multi_split(text):
    return re.split(r'[;,\*\n]', text)

# Check numbers with max 2 decimal places
def check_max_2_decimals(text):
    # Optional leading digits, optional dot and 1-2 digits
    return bool(re.match(r'^\d+(\.\d{1,2})?$', text))

# Advent of Code 2015, Day 5
def is_nice(s):
    # 3 vowels
    vowels = len(re.findall(r'[aeiou]', s)) >= 3
    # double letter
    double = bool(re.search(r'(.)\1', s))
    # non-allowed substrings
    bad = bool(re.search(r'ab|cd|pq|xy', s))
    return vowels and double and not bad

# Advent of Code 2015, Day 6
def translate_line(line):
    # turn on 606,361 through 892,600
    # turn off 448,208 through 645,684
    # toggle 50,472 through 452,788
    pattern = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')
    match = pattern.match(line)
    if match:
        action = match.group(1)
        p1 = (int(match.group(2)), int(match.group(3)))
        p2 = (int(match.group(4)), int(match.group(5)))
        return action, p1, p2
    else:
        raise Exception("Invalid instruction format")

if __name__ == "__main__":
    # Test cases
    print("Testing Regex Exercises...")
    
    # R-numbers
    the_list = ['r0003689', 'u0103828', 'R0001555', 'r001782', '0008750']
    v, inv = check_r_numbers(the_list)
    print(f"Valid: {v}, Invalid: {inv}")
    
    # Numbers
    text1 = "Exercises number 1, 12, 13, 345 and 2453 are important"
    print(f"Nums 1-3: {find_numbers_1_to_3(text1)}")
    
    # Casing
    print(f"Pascal to Snake: {pascal_to_snake('PythonExercises')}")
    print(f"Detect/Convert: {detect_and_convert_casing('python_exercises')} / {detect_and_convert_casing('PythonExercises')}")
    
    # Whitespace
    print(f"Remove space: '{remove_extra_whitespaces('Python      Exercises')}'")
    
    # Split
    print(f"Multi split: {multi_split('The quick brown\\nfox jumps*over the lazy dog.')}")
    
    # Max 2 decimals
    for n in ['123.11', '123.1', '123', '0.21', '123.1214', '3.124587', 'e666.86']:
        print(f"{n}: {check_max_2_decimals(n)}")

    # AoC Day 5
    for s in ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]:
        print(f"is_nice('{s}'): {is_nice(s)}")
        
    # AoC Day 6
    for l in ['turn on 606,361 through 892,600', 'turn off 448,208 through 645,684', 'toggle 50,472 through 452,788']:
        print(f"translate: {translate_line(l)}")
