#ejercicio2 escribe un programa en el que el ordenador elija un numero al azar entre el 1 y 10 y le pida al usuario que intente adivinarlo. si elusuario adivina correctamente el programa debe mostrar"¡correcto!".si no, debe mostrar "sigue intentando". pista: usa una variable para almacenar el numero secreto y utiliza condicionales para comparar el numero ingresado con el numero secreto.
NUM_ALEATORIO=3
print("dime un num del 1 al 10")
numero=int(input())
if(numero==NUM_ALEATORIO):
    print("has acertado")
else:
    print("sigue intentandolo")    
