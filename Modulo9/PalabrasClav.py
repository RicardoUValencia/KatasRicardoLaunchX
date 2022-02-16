# Función con un informe preciso de la misión. 
# Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno

from datetime import timedelta, datetime # Importamos la libreria datetime y timedelta 
# Definimos la hora de prelanzamiento
hora_prelanzamiento = datetime.datetime(2020, 5, 1, 12, 00, 00)
# Definimos el tiempo de vuelo
tiempo_vuelo = datetime.timedelta(hours=5, minutes=30, seconds=00)
# Definimos el destino
destino = "Tierra"
# Definimos el tanque externo
tanque_externo = 100
# Definimos el tanque interno
tanque_interno = 50
# Definimos el tiempo de combustible
tiempo_combustible = tanque_externo - tanque_interno

def informe(hora_prelanzamiento, tiempo_vuelo, destino, tanque_externo, tanque_interno, tiempo_combustible): # Definimos la función
    hora_final = hora_prelanzamiento + tiempo_vuelo # Calculamos la hora final
    hora_final = hora_final.strftime("%H:%M:%S") # Formateamos la hora final
    return f""" 
    La misión ha sido lanzada el día {hora_prelanzamiento.strftime("%d/%m/%Y")} a las {hora_prelanzamiento.strftime("%H:%M:%S")}
    El destino de la misión es {destino}
    El tanque externo tiene {tanque_externo} litros
    El tanque interno tiene {tanque_interno} litros
    El tiempo de combustible es de {tiempo_combustible} litros
    La hora final es {hora_final}
    """ 

# Escribiendo la nueva función de reporte considerando lo anterior
def nuevo_informe(destino, *minutes, **fuelreservations): 
    return f"""Destion: {destino}
    Tiempo de vuelo: {minutes[0]} minutos
    Tanque externo: {fuelreservations['external']} litros
    Tanque interno: {fuelreservations['internal']} litros
    Tiempo de combustible: {fuelreservations['external'] - fuelreservations['internal']} litros
    """ # Retornamos el reporte
print(nuevo_informe("Tierra", 5, external=100, internal=50)) # Escribiendo la nueva funcion de reporte considerando lo anterior

# Escribiendo la nueva funcion
def nuevo_informe(destino, *minutes, **fuelreservations): 
    Reporte_info = f"""Destion: {destino} # 
    Tiempo de vuelo: {minutes[0]} minutos
    Tanque externo: {fuelreservations['external']} litros
    Tanque interno: {fuelreservations['internal']} litros
    Tiempo de combustible: {fuelreservations['external'] - fuelreservations['internal']} litros""" 

    for tanque, litros in fuelreservations.items(): # Recorremos los tanques
        Reporte_info += f"\nTanque {tanque} tiene {litros} litros" # Agregamos el tanque y los litros
    return Reporte_info # Retornamos el reporte

print(nuevo_informe("Tierra", 5, external=100, internal=50, tank1=50, tank2=100)) 

