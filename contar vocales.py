def contar_vocales(oracion):
    # Definir las vocales en minúsculas y mayúsculas
    vocales = 'aeiouAEIOU'
    contador = 0

    # Recorrer cada carácter de la oración
    for letra in oracion:
        if letra in vocales:
            contador += 1
    
    return contador

# Ejemplo de uso
oracion = input("Introduce una oración: ")
print(f"El número de vocales es: {contar_vocales(oracion)}")
