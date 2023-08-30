class Student:

    numar_studenti = 0

    def __init__(self, nume, prenume, medie) :
        self.nume = nume
        self.prenume = prenume
        self.medie = medie
        print ("Initializare student:",self.nume,self.prenume)
        Student.numar_studenti += 1

    def test_bursier(self) :
        if self.medie>=9.50:
            print ("Bursa de merit")
        elif 8.50<=self.medie<9.50:
            print ("Bursa de studiu")

    def nr_studenti():
        print ("Exista",Student.numar_studenti,"instante.")
    nr_studneti = staticmethod(nr_studenti)

student1 = Student('Bucur','Tudor',10)
student1.test_bursier()
Student.nr_studenti()

student2 = Student('Enache','Stefan',8)
student2.test_bursier()
Student.nr_studenti()
