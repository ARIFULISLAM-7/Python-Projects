Assignments = 20
Test = 70
Lab_Works = 10
result = int(input("Enter your marks: "))
if result == 100:
    print("Your grade is A+ , Excellent! You taked the Test, provided Assignments, and did Lab Works.")
elif result >= 90:
    print("Your grade is A , Very Good! You taked the Test, and provided Assignments.")
elif result >= 80:
    print("Your grade is B , Good! You taked the Test, and did Lab works.")
elif result >= 70:
    print("Your grade is C , Average! You taked the Test only.")
else:
    print("Your grade is F , Fail! You did not take the Test, Assignments, and Lab Works.")
