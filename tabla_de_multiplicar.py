# Solicitar un número al usuario
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

# Mostrar la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
