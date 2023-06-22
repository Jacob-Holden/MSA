import student_class

student_data_file = open("student.csv, r")

student_data = {}

for line_of_data in student_data_file:
    keys_values = line_of_data.split(",")
    student_data.append(line_of_data)
student_data_file.close()
for student in student_data:
    student.print_student_data()

student_data_file.close()
    


student1 = student_class.Student("Maya", "Angelou", "Literature", 10, 4.0, 12345)
student2 = student_class.Student("Honda", "Accord", "Engineering", 69, 1.0, 12346)

student_list = []
student_list.append(student1)
student_list.append(student2)



for student in student_list:
    student.print_info()
    