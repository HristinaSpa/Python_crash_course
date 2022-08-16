#Izolirani komandi koda
#When we create the function we use the DEF word
def word():
     print(5+5)
word()


def zbir (a, b):
     if a> 10:
          print(a)
     elif b > 15:
          print(b)
     else:print(a+b)

a = 18
b = 4
zbir(a,b)

def sentence():
 for x in range(1, 11):
  print(x, " Ja znam kako rade funkcije")

sentence()


def recenico ():
    for x in range (1,11):
        print(x, "I am the best")

recenico()


def pozdrav (Hristina):
    print("Bok, "+ Hristina)

ime = input("Hristina")
pozdrav(ime)

def bmi(tezina, visina):
    visina_m = visina/100
    return tezina / (visina_m * visina_m)

tezina = int(input("Unesi tezinu: "))
visina = int(input("Unesi visinu: "))

print(bmi(tezina, visina))

def my_function():
  print("Hello from a function")

def my_function():
  print("Zdravo moeto ime e: ")

my_function()

def my_function():
  print("Zdravo moeto ime e: ")

my_function ()














