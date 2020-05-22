from dbmanager import Db_Manager
from student import Student
from teacher import Teacher


class App:
    def __init__(self):
        self.db = Db_Manager()

    def init_app(self):
        while True:
            choice = input("--*----------*--\nSchool DB Manager v.01\n1-Student List\n2-Teacher List\n3-Add Student"
                           "\n4-Add Teacher\n5-Edit Student\n6-Edit Teacher\n7-Exit\n>>")

            if choice == "1":
                self.display_students()
            elif choice == "2":
                self.display_teachers()
            elif choice == "3":
                self.add_student()
            elif choice == "4":
                self.add_teacher()
            elif choice == "5":
                self.edit_student()
            elif choice == "6":
                self.edit_teacher()
            elif choice == "7":
                break
            else:
                print("Wrong choice")

    def display_students(self):
        classes = self.db.get_classes()
        for i in classes:
            print(f"{i.Id}: {i.Name}")
        classid = input("Which class:\n>>")

        students = self.db.get_students_by_class_id(classid)
        print("Number Name Surname Class")
        i = 1
        for student in students:
            print(f"{i}-)" + student.StudentNumber + "\t", student.Name + "\t", student.Surname + "\t", student.ClassID)
            i += 1

    def display_teachers(self):
        teachers = self.db.get_teachers()
        print("Branch\tName Surname")
        i = 1
        for teacher in teachers:
            print(f"{i}-)" + teacher.Branch, teacher.Name, teacher.Surname)
            i += 1

    def add_student(self):
        s_number = input("Enter Student Number: ")
        name = input("Enter Student Name: ")
        surname = input("Enter Student Surname: ")
        birthday = input("Enter Student Birthday(d/m/y): ")
        gender = input("Enter Student Gender(M/F): ")
        clas_id = int(input("Enter Student Class id: "))

        student = Student(None, s_number, name, surname, birthday, gender, clas_id)
        self.db.add_student(student)

    def add_teacher(self):
        branch = input("Enter Teacher Branch: ")
        name = input("Enter Teacher Name: ")
        surname = input("Enter Teacher Surname: ")
        birthday = input("Enter Teacher Birthday(d/m/y): ")
        gender = input("Enter Teacher Gender(M/F): ")

        teacher = Teacher(None, branch, name, surname, birthday, gender)
        self.db.add_teacher(teacher)

    def edit_student(self):
        self.display_students()
        choice = input("Enter the student number you would like to edit: ")

        name = input("Enter Student Name: ")
        surname = input("Enter Student Surname: ")
        birthday = input("Enter Student Birthday(d/m/y): ")
        gender = input("Enter Student Gender(M/F): ")
        clas_id = int(input("Enter Student Class id: "))

        student = Student(None, choice, name, surname, birthday, gender, clas_id)
        self.db.edit_student(student)

    def edit_teacher(self):
        self.display_teachers()
        choice = input("Enter the teacher id you would like to edit:")

        branch = input("Enter Teacher Branch: ")
        name = input("Enter Teacher Name: ")
        surname = input("Enter Teacher Surname: ")
        birthday = input("Enter Teacher Birthday(d/m/y): ")
        gender = input("Enter Teacher Gender(M/F): ")

        teacher = Teacher(choice, branch, name, surname, birthday, gender)
        self.db.edit_teacher(teacher)

    def delete_student(self):
        pass

    def delete_teacher(self):
        pass


if __name__ == "__main__":
    school_app = App()
    school_app.init_app()
