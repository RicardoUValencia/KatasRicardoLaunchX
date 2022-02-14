from turtle import distance
distanceT = 149597870 # Distancia de la tierra en km
distanceJ = 778547200 # Distancia de Jupiter en km

# Calculamos la distancia entre los dos planetas en km
distance_planetas = abs(distanceT - distanceJ) # abs() devuelve el valor absoluto de un numero
print(distance_planetas)

# Convertimos las distancias de km a millas 
distanceTierra = distanceT * 0.621
distanceJupiter = distanceJ * 0.621

# Imprimimos las distancias en millas
print("La distancia de la tierra es:", distanceTierra, "millas")
print("La distancia de Jupiter es:", distanceJupiter, "millas")

# Calculamos la distancia entre los dos planetas en millas
distance_planetas = abs(distanceT - distanceJ) # abs() devuelve el valor absoluto de un numero
print(distance_planetas)