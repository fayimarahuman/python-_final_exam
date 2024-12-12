def grade_students():
    student_marks=int(input("enter the student's score:\t"))
    if 90<=student_marks<=100:
      print("Grade is A")
    elif 80<=student_marks<=89:
      print("Grade is B")
    elif 70<=student_marks<=79:
       print("grade is C")
    elif 60<=student_marks<=69:
       print("Grade is D")
    else:
      print("F")  
grade_students()      