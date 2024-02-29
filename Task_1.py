student_data = {}  

num_students=int(input("Enter the Number of Students"))
for x in range(num_students):
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        student_data[student_name] = student_id
        
print(student_data)        
        

