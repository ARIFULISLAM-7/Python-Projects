# Dictionary to map drades to their corresponding values
grade_points = {"A+": 4.0,
                "A": 4.0,
                "A-": 3.7,
                "B+": 3.3,
                "B": 3.0,
                "B-": 2.7,
                "C+": 2.3,
                "C": 2.0,
                "C-": 1.7,
                "D+": 1.3,
                "D": 1.0,
                "D-": 0.7,
                "F": 0 }
# prompt the user to enter the number of subjects
num_of_subjects = int(input("Enter the number of subjects: "))
# initialize variables to store the total GPA and the number of subjects
total_gpa = 0
count = 0
# loop through each subjects
while count < num_of_subjects:
# prompt the user to enter the name of the course and the gpa grade
    course = input("Enter the name of the course: ")
    grade = input("Enter the grade: ")
# convert the grade to uppercase to make it non-case sensitive
    grade = grade.upper() # It is a method to make uppercase
# check if the grade is valid
    if grade not in grade_points:
        print("Invalid! Please enter a valid grade point.")
        continue
# print the course and grade
    print(f"{course.capitalize()}: {grade}")
# prompt the user to confirm the entry
    confirmation = input("*Is this entry correct? [Yes/No]")
    if confirmation.lower() != "yes":
        continue
# add the gpa value of the grade to the total GPA
    total_gpa += grade_points[grade]
    count += 1
# calculate the average GPA
average_gpa = total_gpa / count
# print the average GPA
print(f"Average GPA: {average_gpa:.2f}")
