def main():
    try:
        archivo_config = open("config.txt")
        # open("/path/to/config.txt")
    except FileNotFoundError:
        print("Archivo no encontrado")
    except IsADirectoryError:
        print("Se encontro config.txt pero como directorio, No se puede leer")
    except (BlockingIOError, TimeoutError):
        print("El archivo tiene mucha carga y no se puede leer")

# Como primer paso se incluye la excepcion try y except a la funcion creada.
# Corolario: Exception en except es una excepcion para cualquier error que pueda ocurrir.

# Agrupar excepcion de naturaleza similar


if __name__ == "__main__": # Si se ejecuta el archivo como programa principal
    main() # Se ejecuta la funcion main()