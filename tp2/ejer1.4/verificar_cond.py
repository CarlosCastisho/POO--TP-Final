def verif_cond(fun):
    def wrapper(*args, **kwargs):
        for num in args:
            if num > 0:
                print(f"El {num} es positivo")
            else:
                print(f"El {num} es negativo")
        return fun(*args, **kwargs)
    return wrapper

@verif_cond
def numeros(a,b):
    return a + b

print(f"El resultado de la suma es: ", numeros(-3,6))