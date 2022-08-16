#Types of collections we are going to use: Lists and Dictionaries
postenski_broj = [1000, 1001, 1002]
print(postenski_broj)

lista = [1,2,3,4,5,6,]
print(lista)
print(lista[3])

role = "Software tester"
print(role[8])

lista = [1020,30,40,50,60]
for element in lista:
    print(element)


lista = [ 5,6,7,8,9,10]
for element in lista:
    if element == 5 :
        print("Sjedi, odlican!")

lista = [1,2,3,4,5]
for element in lista:
    if element == 4:
        print("You finished on the 4 th place")

#Operatori, osnovni membership so : in ; not in

lista = [1,2,3,4,5]
if 5 in lista:
    print("Sjedi odličan")

lista = ["prvi", "drugi", "treci"]
if "drugi" in lista:
    print("You have finished on the second place!")

# len method (vraca broj svaki objekta)

role ="Software tester"
role_leanth = len(role)
print(role_leanth)

# When you add an element at the end of the list use APPEND
# When you add an element as a last index use INSERT
# REMOVE briše zadni element
# POP ali DEL briše element na odredenom indexu

list =["Ivona","David","Dino","Vanja"]
list.insert(0, "Tomislav")
list.append("Juran")
list.remove("Vanja")
print(list)

list =["Ivona","David","Dino","Vanja"]
if len(list)>3:
    print(list[1],list[3])









