#9° EJERCICIO

import libreria

def blanca():
    input("Ingrese el nombre de la ciudad:")
    print("CIUDAD GUARDADA")

def amistad():
    input("Ingrese el nombre de la ciudad:")
    print("CIUDAD GUARDADA")

def capital():
    input("Ingrese el nombre de la ciudad:")
    print("CIUDAD GUARDADA")

def primavera():
    input("Ingrese el nombre de la ciudad:")
    print("CIUDAD GUARDADA")

def ombligo():
    input("Ingrese el nombre de la ciudad:")
    print("CIUDAD GUARDADA")


opc=0
max=6

while(opc!=max):
    print("############## MENU 9 #################")
    print("#### NOMBRE DE DEPARTAMENTOS  #########")
    print("#-------------------------------------#")
    print("# 1.Ciudad blanca                     #")
    print("# 2.Ciudad de la amistad              #")
    print("# 3.Capital del Perú                  #")
    print("# 4.Ciudad de la eterna primavera     #")
    print("# 5.Ombligo del mundo                 #")
    print("# 6.Salir del menu   ##################")

    opc=libreria.pedir_numero("Ingrese la opcion:",1,6)
    if(opc==1):
        blanca()
    if(opc==2):
        amistad()
    if(opc==3):
        capital()
    if(opc==4):
        primavera()
    if(opc==5):
        ombligo

print("FIN DEL PROGRAMA ")

