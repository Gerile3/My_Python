class Teacher:
    def __init__(self, Id, Branch, Name, Surname, Birthdate, Gender):
        self.Id = Id
        self.Branch = Branch
        self.Name = Name
        self.Surname = Surname
        self.Birthdate = Birthdate
        self.Gender = Gender

    @staticmethod
    def create_teacher(obj):
        listo = []

        if isinstance(obj, tuple):
            listo.append(Teacher(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5]))
        else:
            for i in obj:
                listo.append(Teacher(i[0], i[1], i[2], i[3], i[4], i[5]))

        return listo
