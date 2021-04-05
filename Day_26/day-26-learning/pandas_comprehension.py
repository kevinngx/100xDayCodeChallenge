import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "scores": [71, 82, 90]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)

# Loop through data frame
# for (key, value) in  student_df.items():
#     print(value)

# loop through rows of a data frame
for (index, row) in student_df.iterrows():
    print(row)