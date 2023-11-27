def registro_llamadas(funtion):
    def wrapper(*arg, **kwargs):
        print(f"La funcion: {funtion.__name__} tiene como parametros {arg} y {kwargs}")
        result = funtion(*arg, **kwargs)
        print(f"El resultado es {result}")
        return result
    return wrapper

@registro_llamadas
def suma(a,b):
    return a + b


suma(5,6)
