# EJERCICIO NUMERO 6
import libreria

def ayacucho():
    input("Ingrese año del acontecimiento:")
    print("AÑO GUARDADO")

def independencia():
    input("Ingrese año del acontecimiento:")
    print("AÑO GUARDADO")

def ayacucho():
    input("Ingrese año del acontecimiento:")
    print("AÑO GUARDADO")

opc = 0
max = 4

while (opc != max):
    print("########## # MENU 6  ###########")
    print("## FECHAS HISTORICAS DEL PERU ##")
    print("#------------------------------#")
    print("# 1.año de independencia       #")
    print("# 2.año de batalla de ayacucho #")
    print("# 3.año de guerra del pacifico #")
    print("# 4. Salir del menu ############")

    opc =libreria.pedir_numero("Ingrese opcion:",1,4)
    if(opc==1):
        independencia()
    if(opc==2):
        ayacucho()
    if(opc==3):
        pacifico()
