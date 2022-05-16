# Lista de planetas
planets = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]

# Solicitamos el nombre de un planeta
Nom_Planet = input("Ingrese el nombre del planeta: ")
if Nom_Planet in planets: # Busca si el planeta esta en la lista
    print("El planeta", Nom_Planet, "está en la lista\n") # Mostramos que está en la lista
else: # Si el planeta ingresado no está en la lista
    print("El planeta no está en la lista\n") # Mostramos que no está en la lista

# Busca el planeta en la lista
planeta_index = planets.index(Nom_Planet) # Obtenemos el índice del planeta ingresado
print("El planeta", Nom_Planet, "esta en la posicion", planeta_index) # Mostramos el planeta y su posición en la lista

# Muestra los planetas más cercanos al sol
Planetas_cercanos = planets[:2] # Obtenemos los dos primeros elementos de la lista planets
print("Los planetas más cercanos al sol son: ", Planetas_cercanos) # Mostramos los dos primeros elementos de la lista planets

# Muestra los planetas más lejanos al sol
Planetas_lejanos = planets[6:8] # Obtenemos los dos últimos elementos de la lista planets
print("Los planetas mas lejanos al sol son: ", Planetas_lejanos) # Mostramos los dos últimos elementos de la lista planets
