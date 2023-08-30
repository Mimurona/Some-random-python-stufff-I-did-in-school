def dialog(mesaj, incercari=1) :
    while incercari>0:
        raspuns=input(mesaj)
        if raspuns in ('d','da') :
            rasp=1
            incercari=incercari-1
        if raspuns in ('n','nu') :
            return 0
        return rasp
dialog("Doriti sa iesiti?")
dialog("Sigur doriti sa stergeti fisierul?",2)
