student = {
    "name": "Ankush",
    "age": 23,
    "college": "Rungta college of science and technology"
}


# print(student["age"])

student['nationality'] = "Indian"

# print(student)

# for i in student:
#     print(i,":", student[i])

for key, value in student.items():
    print(key, ":", value)