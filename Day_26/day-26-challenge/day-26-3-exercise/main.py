with open("file1.txt") as file_1:
    data_1 = file_1.read().splitlines()

with open("file2.txt") as file_2:
    data_2 = file_2.read().splitlines()

print(data_1)
print(data_2)

overlap = [n for n in data_1 if (n in data_2)]
print(overlap)