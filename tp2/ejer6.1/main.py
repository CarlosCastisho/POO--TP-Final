def es_primo(num):
    n = 2
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False

def sum_primo(sum_p):
    if sum_p < 2:
        return 0
    elif es_primo(sum_p):
        return sum_p + sum_p(sum_p - 1)
    else:
        return sum_p(sum_p - 1)


print(sum_primo(11))