#1°Primer Ejercicio
import libreria
def jugar_fu():
    input("ingrese campeon de la copa america:")
    print("EQUIPO RECIBIDO")


def jugar_vo():
    input("Numero de jugadores posible:")
    print("NUMERO RECIBIDO")

opc=0
max=3
while(opc!=max):
    print("###### MENU 1 ######")
    print("#------------------#")
    print("# 1.jugar fulbito  #")
    print("# 2.jugar voley    #")
    print("# 3.salir ##########")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        jugar_fu()


    if(opc==2):
        jugar_vo()

print("FIN DEL PROGRAMA")



