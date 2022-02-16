# Definimos la funcion para determinar cuanta agua queda con el transcurso de los dias
def agua(astronautas, agua_por_dia, dias):  # Astronautas, agua por dia, dias
    agua_usada = astronautas * 5 # 5 litros de agua por astronauta
    total_agua = agua_usada * dias # Total de litros de agua
    agua_restante = agua_por_dia - agua_usada # Litros de agua restante
    return f"El agua que queda es {agua_restante * dias} litros" # Retorna el valor de la variable

# Usando excepciones
try: # Se define la excepcion
    agua(5, 10, 5) # 5 astronautas, 10 litros por dia, 5 dias
except RuntimeError as err: # RuntimeError, excepcion para generar la alerta.
    print(f"Error: {err}") # Imprime el error

