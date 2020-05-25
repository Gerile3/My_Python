import sqlite3
from connection import connection
from student import Student
from teacher import Teacher
from classes import Class


class Db_Manager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_students(self):
        sql = "select * from Student"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Student.create_student(obj)
        except sqlite3.Error as err:
            print("Error:", err)

    def get_student_by_id(self, id):
        sql = "select * from student where id = ?"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            return Student.create_student(obj)
        except sqlite3.Error as err:
            print("Error:", err)

    def get_students_by_class_id(self, classid):
        sql = "select * from student where classid = ?"
        value = (classid,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Student.create_student(obj)
        except sqlite3.Error as err:
            print("Error:", err)

    def add_student(self, student: Student):
        sql = "INSERT INTO STUDENT(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES (?, ?, ?, ?, ?, ?)"
        value = (student.StudentNumber, student.Name, student.Surname, student.Birthdate, student.Gender, student.ClassID)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print("{} added to Student database".format(student.Name))
        except sqlite3.Error as err:
            print(err)

    def edit_student(self, student: Student):
        sql = "UPDATE STUDENT SET Name=?,Surname=?,Birthdate=?,Gender=?,ClassId=? WHERE StudentNumber=?"
        value = (student.Name, student.Surname, student.Birthdate, student.Gender, student.ClassID, student.StudentNumber)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print("Changed Student", student.StudentNumber)
        except sqlite3.Error as err:
            print(err)

    def get_teacher_by_id(self, id):
        sql = "select * from teacher where id = ?"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            return Teacher.create_teacher(obj)
        except sqlite3.Error as err:
            print("Error:", err)

    def get_teacher_by_branch(self, branch):
        sql = "select * from Teacher where Branch = ?"
        value = (branch,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Teacher.create_teacher(obj)
        except sqlite3.Error as err:
            print("Error:", err)

    def get_teachers(self):
        sql = "select * from Teacher"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Teacher.create_teacher(obj)
        except sqlite3.Error as err:
            print("Error:", err)

    def add_teacher(self, teacher: Teacher):
        sql = "INSERT INTO Teacher(Branch,Name,Surname,Birthdate,Gender) VALUES (?, ?, ?, ?, ?)"
        value = (teacher.Branch, teacher.Name, teacher.Surname, teacher.Birthdate, teacher.Gender)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print("{} added to Teacher database".format(teacher.Name))
        except sqlite3.Error as err:
            print(err)

    def edit_teacher(self, teacher: Teacher):
        sql = "UPDATE Teacher SET Branch=?,Name=?,Surname=?,Birthdate=?,Gender=? WHERE Id=?"
        value = (teacher.Branch, teacher.Name, teacher.Surname, teacher.Birthdate, teacher.Gender, teacher.Id)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print("Changed Teacher", teacher.Id)
        except sqlite3.Error as err:
            print(err)

    def get_classes(self):
        sql = "select * from Class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.Create_Class(obj)
        except sqlite3.Error as err:
            print("Error:", err)

    def del_student(self, StudentNumber):
        sql = "DELETE FROM STUDENT WHERE StudentNumber=?"
        value = (StudentNumber,)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print("Deleted Student", StudentNumber)
        except sqlite3.Error as err:
            print(err)

    def del_teacher(self, Id):
        sql = "DELETE FROM Teacher WHERE Id=?"
        value = (Id,)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print("Deleted Teacher", Id)
        except sqlite3.Error as err:
            print(err)


if __name__ == "__main__":
    db = Db_Manager()
    # student = db.get_student_by_id(1)
    # print(student[0].Name, student[0].Surname)
    # clas = db.get_students_by_class_id(1)
    # print(clas[0].Name)
    # std = Student(None, 103, "Elif", "Yar", datetime(1990, 2, 3), "K", 1)
    # db.add_student(std)
    # std = Student(None, 103, "Elif", "Karlır", "03/05/1991", "K", 1)
    # db.edit_student(std)
    # tchr = Teacher(None, "Cs", "David", "Mvp", "03/05/1981", "E")
    # db.add_teacher(tchr)
    # tchr = Teacher(5, "Cs", "David", "The_Mvp", "03/05/1981", "E")
    # db.edit_teacher(tchr)
    # teacher = db.get_teacher_by_id(1)
    # teacher2 = db.get_teacher_by_branch("Cs")
    # clas_list = db.get_classes()
    # print(clas_list)
    students = db.get_students()
    for student in students:
        print(student.StudentNumber, student.Name, student.Surname, student.ClassID)
    # teachers = db.get_teachers()
    # for teacher in teachers:
    #     print(teacher.Branch, teacher.Name, teacher.Surname, teacher.Id)
    # # db.del_teacher(3)
    # db.del_student(103)
