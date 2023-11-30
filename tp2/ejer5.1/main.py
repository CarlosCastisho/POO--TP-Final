def suma_dig_par(num):
    cadena_num = str(num)
    sum = 0
    for dig in cadena_num:
        if int(dig) % 2 == 0:
            sum += int(dig)
    return sum

def suma_dig(num_cond):
    if num_cond > 0:
        if num_cond % 2 == 1:
            nuevo_num = num_cond - 3
            return suma_dig_par(nuevo_num)
        elif num_cond % 2 == 0:
            return suma_dig_par(num_cond)
    else:
        if num_cond < 0:
            nuevo_num = num_cond + 1
            return nuevo_num


print(suma_dig(3425672))
print(suma_dig(3425671))
print(suma_dig(-3425672))
