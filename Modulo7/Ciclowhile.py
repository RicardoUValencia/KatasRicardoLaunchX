#Declaramos variables
new_planet = input("Introduce el nombre del planeta: ")

planets = [] # Lista vacia de planetas

#Creacion del ciclo while

while new_planet != "done":
    planets.append(new_planet) # Comprobamos que la variable new_planet contiene un valor
    new_planet = input("Introduce el nombre del nuevo planeta: ")


# Mostramos los planetas
# print("Los planetas introducidos son: ", planets)

