# Question2: Create a "School" class in Python. This class should have the following features and functionality:

# ##### Features:
# - "name"
# - "foundation_year"
# - "students"
# - "teachers"
# -
# ##### Methods:
# - add_new_student(self, student_name, class): A method used to add a new student to the school. It takes the student's name and class and adds it to the "students" list.
# - add_new_teacher(self, teacher_name, branch): A method used to add a new teacher to the school. It takes the teacher's name and major and adds it to the "teachers" dictionary.
# - view_student_list(self): A method used to display the list of students enrolled in the school. List student names and classes.
# - view_teacher_list(self): A method used to display the list of teachers working in the school. List teacher names and majors.

class School:
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = [] #list of students
        self.teachers = {} #dictionary of teachers

    def add_new_student(self, student_name, class_name):
        self.students.append((student_name, class_name))  #add as a tuple

    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch  # key-value 

    def view_students_list(self):
        print("Student List:")
        for name, cls in self.students:
            print(f"{name} - Class: {cls}")

    def view_teacher_list(self):
        print("Teacher List:")
        for name, branch in self.teachers.items():
            print(f"{name} - Branch: {branch}")
    
my_school = School("Hacettepe", 1987)
my_school.add_new_student("Ahmet", "2B")
my_school.add_new_teacher("Jason", "Math")

my_school.view_students_list()
my_school.view_teacher_list()