#Este ejercicio es para pedirle al usuario ingresar nombre de usuario y contraseña
USUARIO_BBDD = "admin"
PASSWORD_BBDD = 1234
print("Escribe un nombre de usuario")
Usuario=(input())
print("Es necesario introducir contraseña")
Contraseña=int(input())

if(Usuario == USUARIO_BBDD) and (Contraseña == PASSWORD_BBDD):
    print("acceso concedido")
else:
    print("acceso denegado")
