import time
def retardo(segundos):
    def retardo(func):
        def wrapper(*args, **kwargs):
            print("Esperando el resultado de la función.......")
            time.sleep(segundos)
            resul = func(*args, **kwargs)
            return resul
        return wrapper
    return retardo 

@retardo(5)
def sum(a,b):
    return a+b

print(sum(4,5))
