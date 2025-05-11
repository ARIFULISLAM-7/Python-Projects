# Assignments = 20
# Test = 70
# Lab_Works = 10
# result = int(input("Enter your marks: "))
# if result == 100:
#     print("Your grade is A+ , Excellent! You taked the Test, provided Assignments, and did Lab Works.")
# elif result >= 90:
#     print("Your grade is A , Very Good! You taked the Test, and provided Assignments.")
# elif result >= 80:
#     print("Your grade is B , Good! You taked the Test, and did Lab works.")
# elif result >= 70:
#     print("Your grade is C , Average! You taked the Test only.")
# else:
#     print("Your grade is F , Fail! You did not take the Test, Assignments, and Lab Works.")

assignment = float(input("Enter your assignment number: "))
test = float(input("Enter your test number: "))
lab = float(input("Enter your lab number: ")) 
final_score = (0.1*assignment) + (0.7*test) + (0.2*lab)
print(final_score)
if final_score >= 90:
    grade = "A"
    print("Your grade is:", grade)
elif final_score >= 80:
    grade = "B"
    print("Your grade is:", grade)
elif final_score >=70:
    grade = "C"
    print("Your grade is:", grade)
elif final_score <= 50:
    grade = "D"
    print("Your grade is", grade)
else:
    print(" You are failed.")

