class Cambiar_Dev:
    def __init__(self):
        pass
    
    def __enter__(self):
        print("Cambiando el directorio")
        return self

    def __exit__(self, type, value, traceback):
        print("Saliendo del directorio")

with Entrar_Salir():
    res = 10-4
    print(res)