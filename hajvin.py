#1 Feladat
'''


szamok = list()      #Ezek is jó megoldások
beker = "1"
while be != "":
    beker = input("Kérek egy számot: ")
    if not beker == "": 
        szamok.append(float(beker))



szamok = list()
ismeteld = True
while ismeteld:
    beker = input("Kérek egy számot: ")
    if beker == "":
        ismeteld = False
    else: 
        szamok.append(float(beker))


szamok = list()

while True:
    beker = input("Kérek egy számot: ")
    if beker == "":
        break
    else: 
        szamok.append(float(beker))
print(szamok)
print("-------------------1. feladat--------------------")
print(f"A listában {min(szamok)} a legkissebb")
print(f"A listában {max(szamok)} a legnagyobb")

mini = szamok[0]
for szam in szamok:
    if szam < mini:
        mini = szam 



maxi = szamok[0]
for szam in szamok:
    if szam > maxi:
        maxi = szam 

print(f"A listában {mini} a legkissebb")
print(f"A listában {maxi} a legnagyobb")
'''


#2. a feladat

def harommal_oszthato(lista):
    db = 0
    for szam in lista:
        if szam % 3 == 0:
            db += 1
    return db 

#2. b feladat
import random

szamok = list()
for i in range(20):
    szamok.append(random.randint(1,100))


#2. c feladat

print("	------------- 2.c feladat -------------")
print(f"A listában {harommal_oszthato(szamok)} darab hárommal osztható szám szerepelt.")
















