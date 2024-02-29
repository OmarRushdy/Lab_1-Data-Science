student_data = {}  
student_gpa = {}

num_students=int(input("Enter the Number of Students: "))
for x in range(num_students):
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        student_GPA = input("Enter student GPA: ")
        student_data[student_name] = student_id
        student_gpa[student_name] = student_GPA

print(student_data)        
print(student_gpa)

# https://github.com/OmarRushdy/Lab_1-Data-Science

# updated by omarrwalid