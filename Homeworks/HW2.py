student_count = 2
mark_information = [[0 for i in range(3)] for j in range(student_count)]
student_information = [[0 for a in range(2)] for b in range(student_count)]

for count in range(student_count):
    for notes in range(3):
        if notes == 0:
            mark_information[count][notes] = int(input(f"{count + 1}. student midterm information:"))

        if notes == 1:
            mark_information[count][notes] = int(input(f"{count + 1}. student final information:"))

        if notes == 2:
            mark_information[count][notes] = int(input(f"{count + 1}. student homework information:"))

    for info_student in range(2):
        if info_student == 0:
            student_information[count][info_student] = (input(f"{count + 1}. student name information:"))

        if info_student == 1:
            student_information[count][info_student] = (input(f"{count + 1}. student surname information:"))

info = dict()
max_not = 0


for i in range(student_count):
    note = (mark_information[i][0] + mark_information[i][1] + mark_information[i][2]) / 3
    name_surname = (student_information[i][0], student_information[i][1])
    info[name_surname] = note
    if max_not < note:
        max_not = note
        max_student = (student_information[i][0], student_information[i][1])


information = sorted(info.values())

print("Sorting:")
for info_mark in information:
    print(info_mark, end=" ")

print("\nCongratulations:", max_student)

