grade = int(input("Enter your rating : "))

if grade >= 0 and grade <= 100:
    if grade >= 90 and grade <= 100:
        print("student grade is A")
    elif grade >= 80 and grade <= 89:
        print("student grade is B")
    elif grade >= 70 and grade <= 79:
        print("student grade is C")
    elif grade >= 60 and grade <= 69:
        print("student grade is D")
    else:
        print("student grade is F")

    
    

