# El usuario ingresa las distancias de los planetas en cadena de texto
dis_planeta1 = input("Ingrese distancia al planeta 1: ")
dis_planeta2 = input("Ingrese distancia al planeta 2: ")

# Convierte las cadenas de ambos planetas a números enteros
valor1 = int(dis_planeta1)
valor2 = int(dis_planeta2)

# Calcula la distancia entre ambos planetas en km
distancia = abs(valor1 - valor2) # abs() devuelve el valor absoluto de un numero en caso de que el usuario ingrese un valor negativo
print("La distancia entre los planetas en km es: ",distancia)

# Convierte la distancia de km a millas
distancia_millas1 = valor1 * 0.621
distancia_millas2 = valor2 * 0.621

# Calcula la distancia entre ambos planetas en millas
distancia_millas = abs(distancia_millas1 - distancia_millas2) # abs() devuelve el valor absoluto de un numero en caso de que el usuario ingrese un valor negativo
print("La distancia entre los planetas en millas es: ",distancia_millas)
