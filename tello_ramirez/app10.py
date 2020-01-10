#10° EJERCICIO
import libreria

def primera():
    input("Ingrese primer pais :")
    print("PAIS GUARDADO")

def segunda():
    input("Ingrese segundo pais:")
    print("PAIS GUARDADO")

def tercera():
    input("Ingrese tercer pais:")
    print("PAIS GUARDADO")

def cuarta():
    input("Ingrese cuarto pais:")
    print("PAIS GUARDADO")

def quinta():
    input("Ingrese quinto pais:")
    print("PAIS GUARDADO")

def sexta():
    input("Ingrese sexto pais:")
    print("PAIS GUARDADO")

def septima():
    input("Ingrese septimo pais")
    print("PAIS GUARDADO")

def octava():
    input("Ingrese octavo pais:")
    print("PAIS GUARDADO")

def novena():
    input("Ingrese noveno pais:")
    print("PAIS GUARDADO")

def decima():
    input("Ingrese decimo pais:")
    print("PAIS GUARDADO")


opc=0
max=11

while(opc!=max):
    print("######### MENU 10 ########")
    print("## PAISES SUDAMERICANOS ##")
    print("#------------------------#")
    print("# 1.Primer pais          #")
    print("# 2.Segundo pais         #")
    print("# 3.Tercer pais          #")
    print("# 4.Cuarto pais          #")
    print("# 5.Quinto pais          #")
    print("# 6.Sexto pais           #")
    print("# 7.Septimo pais         #")
    print("# 8.Octavo pais          #")
    print("# 9.Noveno pais          #")
    print("# 10.Decimo pais         #")
    print("# 11.Salir del menu  #####")

    opc=libreria.pedir_numero("Ingrese opcion:",1,11)
    if(opc==1):
        primera()
    if(opc==2):
        segunda()
    if(opc==3):
        tercera()
    if(opc==4):
        cuarta()
    if(opc==5):
        quinta()
    if(opc==6):
        sexta()
    if(opc==7):
        septima()
    if(opc==8):
        octava()
    if(opc==9):
        novena()
    if(opc==10):
        decima

print("FIN DEL PROGRAMA ")
