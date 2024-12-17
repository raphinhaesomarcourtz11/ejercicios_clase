def bucle_infinito():
    no_fin = True
    while no_fin:
        respuesta = input("escribe algo: ")
        if(respuesta == "hola"):
            print("has dicho hola")
        elif(respuesta == "fin"):
            print("has terminado")
            no_fin = False 
            
bucle_infinito()