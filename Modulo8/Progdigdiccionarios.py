# Diccionario de planetas y lunas
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# El numero de elementos del diccionario
print("El numero de elementos del diccionario es: ", len(planet_moons))

# Iteramos sobre el diccionario con un ciclo for, es decir, determinamos el numero de lunas
for moons in planet_moons.values():
    planets = len(planet_moons.keys()) # Numero de planetas
    print("El numero de lunas es: ", moons)

# Contamos el numero de lunas
total_moons = 0
for moons in total_moons:
    total_moons += moons
    prom = total_moons / planets
print("El promedio es: ", prom)

