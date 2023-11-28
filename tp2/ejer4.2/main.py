lista_str = ["auto", "avión", "bicicleta"]

mayus = lambda a: a.upper()

resul_mayus = list(map(mayus, lista_str))

print(resul_mayus)