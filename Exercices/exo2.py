#coding: utf-8
a = []
b = int(input("Entrer un nombre de départ : "))
c = int(input("Entrer un nombre d'arrivée : "))
d = int(input("Entrer un pas : "))
a.extend([b, c, d])
print(a)
tab2 = list(range(b, c, d))
a.extend(tab2)
print(a)
print(a[-d:])

