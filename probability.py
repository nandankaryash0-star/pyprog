score = float(input("Enter probsbility score (0.0 - 1.0):  "))

if score <= 1.0:
    if score > 0.8 :
        print("It's a Dog")

    elif score < 0.2 :
        print("It's a Cat")

    else:
        print("It's is Unsure ")

else:
    print("The Score is invalid")