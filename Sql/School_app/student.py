class Student:
    def __init__(self, Id, StudentNumber, Name, Surname, Birthdate, Gender, ClassId):
        self.Id = Id
        self.StudentNumber = StudentNumber
        self.Name = Name
        self.Surname = Surname
        self.Birthdate = Birthdate
        self.Gender = Gender
        self.ClassID = ClassId

    @staticmethod
    def create_student(obj):
        listo = []

        if isinstance(obj, tuple):
            listo.append(Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6]))
        else:
            for i in obj:
                listo.append(Student(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

        return listo
