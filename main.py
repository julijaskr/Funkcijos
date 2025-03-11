import math
import random
import re
import string


#
#
# def print_list_col(arr):
#     for i, num in enumerate(arr):
#         print(f"i-{i}, num-{num}")
#
#
# def print_list_row_i_val(arr):
#     row = ""
#     for i, num in enumerate(arr):
#         row += f"[{i}/{num}], "
#     print(row)
#
#
# arr = [1,5,10,14,20,6,8,10]
#
# print_list_row_i_val(arr)
#
# students_grades = [8,9,10,10,4,8,10,3,8,5,8]
#
# print_list_row_i_val(students_grades)
#
# print_list_col(students_grades)
#
# print_list_col(students_grades)
#
# def say_hi():#nieko nepriima, nieko negrazina
#     print("hi")
#
# say_hi()
#
# def say_hi_to(name):#priima viena kintamaji, nieko negrazina
#     print(f"hi, {name}")
#
# say_hi_to("Jonas")
# say_hi_to("Rolandas")
#
# vardas = "Julija"
# say_hi_to(vardas)
# vardas = "Jonas"
# say_hi_to(vardas)
#
# def sim_pi():#nieko nepriima, bet GRAZINA reiksme I TEN kur buvo iskviesta
#     return 3.1415
#
# pi_val = sim_pi()
# print(pi_val)
# print(sim_pi())
# print(math.pi)
#
# def make_initials(name, surname):# priima DU kintamuosius ir grazina reiksme
#     return (name[0] + surname[0]).upper()
#
# pavarde = "Marozaitis"
# initials = make_initials(vardas, pavarde)
#
# print(initials)
#
# def add_numbers(a = 0, b = 0):# su defaultinemis reiksmemis
#     return a + b
#
# print(add_numbers()) #nieko nepadaviau, suveike dvi defaultines reiksmes
# print(add_numbers(10))#padaviau 1 sk, ji priskyre kintamajam a, b gavo default reiskme
# print(add_numbers(b=10))#padaviau 1 sk, nurodiau, kad ji bus priskirta b kintamajam. a gavo default reiskme
#
# sk = 61852.32150653649853
# print(round(sk))
# print(round(sk, 2))
# print(round(sk, 5))
#
# def generateRndStr(length):
#   symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
#   text = ""
#   for i in range(length):
#     text += symbols[random.randint(0,len(symbols) -1) ]
#   return text
#
# rnd_str = generateRndStr(10)
# print(rnd_str)

# # Sukurkite Funkciją kuri priima du int tipo kintamuosius. Juos susumuoja ir atspausdina.
# def make_initials(name, surname):# priima DU kintamuosius ir grazina reiksme
#     return (name[0] + surname[0]).upper()
#
# pavarde = "Marozaitis"
# initials = make_initials(vardas, pavarde)

# print(initials)
def make_junginys(sk_1, sk_2):
    return int(sk_1) + int(sk_2)
sk_1 = "15"
sk_2 = "35"

junginys = make_junginys(sk_1, sk_2)
print(junginys)

# Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina float tipo reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
def generateRndStr(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text
random_1 = generateRndStr(10)
print(random_1)

# Sukurkite Funkciją kuri priima du int tipo kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
def make_sandauga(sk_1, sk_2):
    return int(sk_1) * int(sk_2)
sk_1 = "9"
sk_2 = "9"
sandauga = make_sandauga(sk_1, sk_2)
print(sandauga)

# Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
def eilute_masyvas(arr):
    for sk in arr:
        print(sk, end=" ")
arr = [4,2,7,1,9]
eilute_masyvas(arr)
print()

# Sukurkite Funkciją kuri priima du int tipo kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.
def sugeneruoti_random(min_value, max_value):
    return random.randint(min_value, max_value)
min_value = 4
max_value = 16
random_sk = sugeneruoti_random(min_value, max_value)
print(random_sk)

# Sukurkite Funkciją kuri sugeneruotų random int skaičių masyvą ir jį gražintų. Funkcija priima tris int tipo kintamuosius, min, max ir length reikšmėms nustatyti.
def sugeneruoti_random_1(min_value_1, max_value_1, length):
    random_skaiciai = []
    for sk_3 in range(length):
        random_skaiciai.append(random.randint(min_value_1, max_value_1))
    return random_skaiciai
min_value_1 = 2
max_value_1 = 20
length = 4
random_sk_1 = sugeneruoti_random_1(min_value_1, max_value_1, length)
print(random_sk_1)

# Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę
kintamasis_7 = sum(random_sk_1)
def kintamas_masyvas(kintamasis_7):
    for sk_7 in kintamasis_7:
        kintamasis_7 = random_sk_1
        kintamasis_7.append(int(sk_7))
    return(kintamasis_7)
print(kintamasis_7)

# Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį (double).
kintamasis_8 = sum(random_sk_1)/ len(random_sk_1)
def vidurkis(kintamasis_8):
    for sk_8 in kintamasis_8:
        kintamasis_8 = random_sk_1
        kintamasis_8.append(int(sk_8))
    return(kintamasis_8)
print(kintamasis_8)

# Sukurkite Funkciją kuri priimtų du int skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis. Pirmas int - išoriniam ciklui, antras vidiniam.
def staciakampis(x, y):
    for i in range(x):
        for j in range(y):
            print('*', end='')
        print()
x = 4
y = 3
staciakampis(x, y)

# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų. Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)
sakinys = "Šiandien labai graži diena"
def skaiciuoti_raides_ir_tarpus(sakinys):
    raides = 0
    tarpai = 0
    for simbolis in sakinys:
        if simbolis.isalpha():
            raides += 1
        elif simbolis == " ":
            tarpai += 1
    return raides, tarpai
raides, tarpai = skaiciuoti_raides_ir_tarpus(sakinys)
print(f"Raidžių skaičius: {raides}")
print(f"Tarpų skaičius: {tarpai}")

# Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.
def sakinys_atbulai(sakinys):
    return sakinys [::-1]
uzkoduotas_sakinys = sakinys_atbulai(sakinys)
print(uzkoduotas_sakinys)

# Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir gale. PVZ (---labas---)
tekstas = "labas"
def konsoleje(tekstas):
    print(f'---{tekstas}---')
konsoleje(tekstas)

# Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu. Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75]. (apačioje yra funkcija, ją nusikopijuokite ir paleiskite, ji sugeneruos stringą, su kuriuo dirbsite)
import random
import re
def generateRndStr(length):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
    text = ""
    for i in range(length):
        text += symbols[random.randint(0, len(symbols) - 1)]
    return text

# Funkcija skaičių apgaubimui laužtiniais skliaustais
def apgaubti_skaicius(tekstas):
    return re.sub(r'(\d+)', r'[\1]', tekstas)  # Suranda skaičius ir apgaubia [ ]

# Generuojame stringą
atsitiktinis_stringas = generateRndStr(10)
uzkoduotas_stringas = apgaubti_skaicius(atsitiktinis_stringas)

# Atspausdiname simbolius stulpeliu
i = 0
while i < len(uzkoduotas_stringas):
    if uzkoduotas_stringas[i] == '[':  # Jei prasideda skaičių grupė
        sk_bloskas = ''
        while i < len(uzkoduotas_stringas) and uzkoduotas_stringas[i] != ']':
            sk_bloskas += uzkoduotas_stringas[i]
            i += 1
        sk_bloskas += ']'  # Pridedame uždarymo skliaustą
        print(sk_bloskas)
    else:
        print(uzkoduotas_stringas[i])  # Spausdiname simbolį
    i += 1

# Parašykite funkciją, kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių jos argumentas dalijasi be liekanos (išskyrus vienetą ir patį save). Pvz padavus 10 turi grąžinti 2,  o padavus 20 gražintų 3.
def skaiciuoti_daliklius(n):
    dalikliai = 0
    for i in range(2, n):
        if n % i == 0:
            dalikliai += 1
    return dalikliai

print(skaiciuoti_daliklius(10))
print(skaiciuoti_daliklius(74)) # dalinasi is 2,4,5,10 = 4
print("=============")
# Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77. Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka, panaudodami trečio uždavinio funkciją.
def atsitiktiniu_sk_kurimas():
    atsitiktiniai_skaiciai = []
    for i in range(100):
        atsitiktiniai_skaiciai.append(random.randint(33, 77))
    return atsitiktiniai_skaiciai

def count_divisors(n):
    dalikliai = 0
    for i in range(2, n):
        if n % i == 0:
            dalikliai += 1
    return dalikliai

atsitiktiniai_skaiciai = atsitiktiniu_sk_kurimas()
print(atsitiktiniai_skaiciai)
dalikliu_skaicius = []
for x in atsitiktiniai_skaiciai:
    dalikliu_skaicius.append(count_divisors(x))
print(dalikliu_skaicius)

dalikliu_skaicius.sort(reverse=True)
print(dalikliu_skaicius)