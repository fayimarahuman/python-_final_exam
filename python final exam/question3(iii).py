def grade_students(students_marks):
    if 90<=students_marks<=100:
      print("Grade is A")
    elif 80<=students_marks<=89:
      print("Grade is B")
    elif 70<=students_marks<=79:
       print("grade is C")
    elif 60<=students_marks<=69:
       print("Grade is D")
    else:
      print("F")  
grade_students(85)  