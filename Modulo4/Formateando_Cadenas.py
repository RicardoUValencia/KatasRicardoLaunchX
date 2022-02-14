# Datos 
name = "Ganimedes"
gravity = 0.00143 #in kms
planeth = "Marte"

texto = """The %s is a satellite of the %s with %s gravitational force.""" % (name, gravity, planeth) # Formateando cadena
texto.upper() # Convierte a mayusculas
texto.title() # Convierte a titulo
print(texto) # Imprime el texto

print(f'The {name} is a satellite of the {planeth} with {gravity*1000} m/s^2 gravitational force.') # Formateando cadena con f-string

# Uniendo titulo y hechos
print('The %s is a satellite of the %s with %s gravitational force.').format(name, planeth, gravity*1000)