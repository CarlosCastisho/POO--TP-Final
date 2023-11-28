lista_str = ["auto", "avión", "bicicleta"]

long = lambda a : len(a)

resul_long = list(map(long,lista_str))

print(resul_long)