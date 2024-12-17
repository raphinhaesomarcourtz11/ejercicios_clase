def suma(a, b):
    resultado = a+b
    return resultado
print("el resultado es",suma(4, 5))

#esto es una funcion que nos calcula el siguiente
def siguiente(resultado):
    resultado = resultado + 1
    return resultado
print("el resultado es",siguiente(41))

def mayor_de_tres(a, b, c):
    if(a>b):
        if(a>c):
            return a 
        else:
            return c 
    else:
        if(b>c):
            return b
        else:
            return c
print("el mayor de tres es",mayor_de_tres(11,25,20))





