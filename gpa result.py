result = int(input("Enter your marks: "))
if result >= 90:
    print("Your GPA is A, Excellent!")
elif result >= 80:
    print("Your GPA is B, Good job!")
elif result >= 70:
    print("Your GPA is C, Keep it up!")
elif result >= 60:
    print("Your GPA is D, You can do better!")
else:
    print("Your GPA is F, Failed!")

for result in range(1, 11):
    print("This is a loop iteration number:", i)
    if result == 90:
        print("Loop has reached halfway point.")
        break
    else:
        print("Loop is still running.")