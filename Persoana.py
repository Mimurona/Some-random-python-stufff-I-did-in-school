class Persoana:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def descrie(self):
        print (self.nume,"are",self.varsta,"ani.")

class profesor(Persoana):
    def __init__(self, nume, varsta, salariu):
        Persoana.__init__(self, nume, varsta)
        self.salariu = salariu

    def descrie(self):
        Persoana.descrie(self)
        print (self.nume,"are salariul:",self.salariu)

class student(Persoana):
    def __init__(self, nume, varsta, medie) :
        Persoana.__init__(self, nume, varsta)
        self.medie = medie

    def descrie(self):
        Persoana.descrie(self)
        print ("Media studentului",self.nume,"este:",self.medie)

p = profesor('Prof. Emil Marinescu', 40, 30000)
s = student('Popescu Daniela', 25, 8.66)

membri = [p, s]
for membru in membri:
    membru.descrie()
        
