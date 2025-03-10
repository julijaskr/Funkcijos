import math
import random
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
