# Creacion de un diccionario llamado planet
planet = {
    'name': 'Mars',
    'moons': 2
}

# Mostrando el nombre del planeta y el numero de lunas
print("El planeta es: " , planet['name'] , " y tiene " , planet.get('moons') , " lunas.")

# Actualizando diccionario (Agregando un nuevo valor)
planet['circunferencia (km)'] = ({
    'polar': 6752,
    'equatorial': 6792
})

# Impresion del planeta con su circunferencia polar
print("El nombre del planeta es: ", planet.get('name'), " con una circunferencia de:", planet['circunferencia (km)']['polar'], "km.")
