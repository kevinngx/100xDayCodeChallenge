# Numbers
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

# String
name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

# Range 
range(1, 5)
range_list = [n * 2 for n in range(1, 5)]
print(range_list)

# Names
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

# Formatting names
all_caps = [name.upper() for name in names if len(name) > 4]
print(all_caps)

