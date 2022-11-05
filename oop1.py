class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


    def get_grade(self):
        return self.grade

class Course(Student):
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1=Student("Genti", 45, 95)
s2=Student("Aldo", 33, 90)
s3=Student("Ambra", 15, 75)
s4=Student("Erla", 11, 60)
s5=Student("Elian", 18, 30)


course = Course("Science", 9)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
course.add_student(s4)
course.add_student(s5)
print(course.get_average_grade())
print(course.add_student(s5))
print(course.students[5].name)