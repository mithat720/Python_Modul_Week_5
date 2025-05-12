class School:
    def __init__(self, name, foundation_year,students=[],teachers={}):
        self.name = name
        self.foundation_year = foundation_year
        self.students = students
        self.teachers = teachers

    def add_new_student(self, student_name, Class):
        self.students.append((student_name, Class))
        print( "Student: {}, Class: {} okula eklendi. ".format(student_name,Class))

    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name]=branch
        print( "Teacher: {}, branch: {} okula eklendi. ".format(teacher_name, branch))

    def view_teacher_list(self):
        print("\nTeacher list")
        for teacher_name,branch in self.teachers.items():
            print(f"Teacher Name:{teacher_name}, Branch: {branch}")

    def view_student_list(self):
        print("\nStudent list")
        for i in self.students:
            print(f"Student Name: {i[0]}, Class: {i[1]}")

School1= School("Maltepe",1972)

School1.add_new_teacher("Ahmet", "biology")
School1.add_new_teacher("suleyman","english")

School1.add_new_student("Mike", "1A")
School1.add_new_student('mert',"1B")

School1.view_student_list()
School1.view_teacher_list()
