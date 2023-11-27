def verificar_tipos(func):
    def wrapper(*args, **kwargs):
        for arg, tipo in func.__annotations__.items():
            if not isinstance(arg, tipo):
                raise TypeError("La función ",args, "debe ser de tipo ", tipo)
        resul = func(*args, **kwargs)
        return resul
    return wrapper

@verificar_tipos
def tipos_func(a:int, b:int) -> int:
    return a + b

print(tipos_func(4,"d"))