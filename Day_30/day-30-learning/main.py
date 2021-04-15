
# File not Found
# with open("a_file.txt") as file:
#     file.read()

# # KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

# # IndexError
# fruit_list = ["Apple", "Bananna", "Pear"]
# fruit = fruit_list[3]

# # Type Error
# text = "abd"
# print(text + 5)

# print("Running")
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     value = a_dictionary["key"]
# except FileNotFoundError:
#     # Never use a bare except clause --> ignores all errors
#     print("File does not exist, creating new file...")
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise TypeError

height = float(input("height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("Human height should not exceed 3m")

bmi = weight / height ** 2
print(bmi)

