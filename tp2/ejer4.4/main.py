import math
list_num = [1, 4, 9, 16, 25, 36]

raiz_cua = lambda x: math.sqrt(x)

resul = list(map(raiz_cua, list_num))

print(resul)
