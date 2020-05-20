class Class:
    def __init__(self, Id, Name, TeacherId):
        self.Id = Id
        self.Name = Name
        self.TeacherId = TeacherId

    @staticmethod
    def Create_Class(obj):
        listo = []
        for i in obj:
            listo.append(Class(i[0], i[1], i[2]))
        return listo
