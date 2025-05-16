class school:
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}

# Sınıfa öğrenci ekleme metodu
    def add_new_student(self, student_name, student_class):
        self.students.append({"name": student_name, "class": student_class})
        print(f"{student_name} adlı öğrenci {student_class}. sınıfa eklendi.")

# Öğrtemen ekleme metodu
    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch
        print(f"{teacher_name} adlı öğretmen {branch} branşına eklendi.")

# Öğrencileri listemelem metodu
    def view_student_list(self):
        print("\nÖğrenci Listesi:")
        for student in self.students:
            print(f"Öğrenci Adı: {student['name']}, Sınıf: {student['class']}")
    
# Öğretmenleri listemeleme metodu
    def view_teacher_list(self):
        print("\nÖğretmen Listesi:")
        for teacher, branch in self.teachers.items():
            print(f"Öğretmen Adı: {teacher}, Branş: {branch}")

# Opsiyonel Okul bilgilerini gösterme metodu    
    def view_school_info(self):
        print("\nOkul Bilgileri:")
        print(f"Okul Adı: {self.name}, Kuruluş Yılı: {self.foundation_year}")


my_school = school("Örnek Okul", 2023)
my_school.add_new_student("Ali", 5)
my_school.add_new_student("Ayşe", 6)
my_school.add_new_teacher("Ahmet", "Matematik")
my_school.add_new_teacher("Fatma", "Fen Bilgisi")
my_school.view_school_info()
my_school.view_student_list()
my_school.view_teacher_list()
