from dbmanager import Db_Manager


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
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                pass
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


if __name__ == "__main__":
    school_app = App()
    school_app.init_app()
