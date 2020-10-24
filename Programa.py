from FechaHora import FechaHora

def zero():
    print("\n\t\t\t --------- FIN DEL PROGRAMA ---------")

def one(UnaFecha,OtraFecha):

    suma= UnaFecha + OtraFecha
    print ('Suma Hora 1 + Hora 2',suma)

def two(UnaFecha,OtraFecha):
    resta= UnaFecha - OtraFecha
    print("Resta HORA 1 - HORA 2", resta)

def three(UnaFecha,OtraFecha):

    mayor= UnaFecha > OtraFecha
    print("Compara Hora1 > Hora 2", mayor)
    print("\tES LA MAYOR")


switcher = {
    0: zero,
    1: one,
    2: two,
    3: three
 }

def switch(argument,UnaFecha,OtraFecha):
    func = switcher.get(argument, lambda x,y: print('\t\t\t\t\t\t\t>> Opción Incorrecta <<\n----------------------------------------------------------------------------------\n'))
    func(UnaFecha,OtraFecha)

if __name__ == '__main__':


    UnaFecha = FechaHora()
    UnaFecha.ponerEnHora(13, 17, 27)

    OtraFecha = FechaHora()
    OtraFecha.ponerEnHora(22, 12, 21)

    bandera = False  # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print('\t\t###############################')
        print("\t\t# 0- SALIR                    #")
        print("\t\t# 1- SUMAR HORA               #")
        print("\t\t# 2- RESTAR HORA              #")
        print('\t\t# 3- MAYOR ENTRE DOS HORAS    #')
        print('\t\t###############################')
        opcion= int(input("\n\t\t>>Ingrese una opción:  "))
        print('\n----------------------------------------------------------------------------------')
        switch(opcion,UnaFecha,OtraFecha)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú