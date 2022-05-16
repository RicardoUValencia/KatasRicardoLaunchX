# Función para leer 3 tanques de combustible y muestre el promedio
def combustible(tanque1, tanque2, tanque3):
    prom = (tanque1 + tanque2 + tanque3) / 3
    return prom

# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))
print(combustible(10, 20, 30))

# Funcion promedio
def promedio(values): 
    prom = sum(values) / len(values) # Calculamos el promedio
    return prom # Retornamos el promedio
print(promedio([22, 25, 31])) 

# Actualiza la funcion
def combustible(tanque1, tanque2, tanque3): 
    prom = (tanque1 + tanque2 + tanque3) / 3 # Calculamos el promedio
    return f"""El promedio es: {prom([tanque1, tanque2, tanque3])}""" # Retornamos el promedio
print(combustible(35, 53, 30)) 

