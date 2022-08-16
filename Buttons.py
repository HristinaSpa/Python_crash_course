#while  and for petlje
#Napishite while petju koja ispisue prvih 100 broja (o-100)

counter= 0
while counter <= 100:
    print(counter)
    counter += 1

# for item in collection --- do something
# for counter in range (0,10) --- do something

#example

string = "Juran je tmuran "
for letter in string:
    if letter == "t":
        print("Ma nema shanse")


string = "I am the best student in the class"
for letter in string:
    if letter == "a":
        print("I got a credentials for this")

string ="Today it is a very hot day"
for letter in string:
    if letter == "z":
        print("Today is a very cold day")


list = ["Ananas", "Banana", "Apple"]
for element in list:
    if element == "Banana":
        print("I am yellow!")

list = [ "Ana", "Bana", "Cana","Dana"]
for element in list:
    if element == "Bana":
        print("This is the oldest member in the group")

