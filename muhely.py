'''
Az adatok beolvasása fájlból,
egy-egy sor az 'adatok' nevű lista egy-egy eleme
'''
adatok = []
with open('autok_listaja.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # strip() metódus eltávolítja a sorvégi \n-t
        adatok.append(sor.strip())


'''
A 'autok' nevű lista 'auto' nevű szótár típusokat fog tartalmazni,
egy autó adatait egy szótár tárolja
'''
auto = {}  # egy auto adatai
autok = []  # szótárakat tartalmazó lista
for elem in adatok:
    auto_adatai = elem.split()
    auto['rendszam'] = auto_adatai[0]
    auto['marka'] = auto_adatai[1]
    auto['tipus'] = auto_adatai[2]
    auto['kor'] = int(auto_adatai[3])
    if auto_adatai[4] == '1':
        auto['javitva'] = True
    else:
        auto['javitva'] = False
    auto['koltseg'] = int(auto_adatai[5])

    autok.append(auto)
    auto = {}  # egy új, üres szótár objektum deklarálása ugyanazon a néven

#print(autok)



#3. a feladat


auto = autok[0]

for au in autok:
    if auto['kor'] < au['kor']:
        auto = au

kor = 0
rendsz = ""
tip = ""
for au in autok:
     if kor < au['kor']:
        kor = au['kor']
        rendsz = au['rendszam']
        tup = au['tipus']

print(auto)
print("    ------------- 3.a feladat -------------")
print(f"A legöregebb autó: {auto['rendszam']},{auto['marka']} {auto['tipus']}, {auto['kor']} éves.")



#3. b feladat


osszeg = 0
for au in autok:
    osszeg += au['koltseg']
    

print("    ------------- 3.b feladat -------------")
print(f"Az egy autóra jutó átlagos javítási költség: {osszeg/len(autok)} Ft.")



#3. c feladat 
print("    ------------- 3.c feladat -------------")

rendszam = input("Adjon meg egy rendszámot (pl. ABC-123)!")
van = False
index = 0
while not van and index < len(autok):
    if autok[index]['rendszam'] == rendszam:
        van = True
    else:
        index += 1
        
if van:
    print("A megadott rendszámú autó a műhelyben van.")








