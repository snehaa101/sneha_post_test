# CREATE SET OF 6 STUDENTS (WITH 2 DUPLICATES )
student = ("lily", "hope", "kalus", "lily", "hope", "elena")

# REMOVE THE DUPLICATES
print("The student sets (2 deplicates removes) : ", student)

# ADD 2 NEW STUDENTS
student.update("elijah", "stefan")

# CREATE A DICTIONARY OF 4 STUDENTS WITH THEIR MARKS
student_marks = {"lily": 80, "hope": 70, "ale": 50, "sana": 40}

# LOOP THROUGH DICTIONARY
for names, marks in student_marks.items():
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("Pass")
    else:
        print("Fail")
