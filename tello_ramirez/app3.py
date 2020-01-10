#3° Ejercicio

import libreria

def cuadrilatero():
    input("Ingrese numero de lados:")
    print("LADOS GUARDADOS")
def triangulo():
    input("Ingrese numero de lados:")
    print("LADOS GUARDADOS")
def pentagono():
    input("Ingrese numero de lados:")
    print("LADOS GUARDADOS")
def octagono():
    input("Ingrese numero de lados:")
    print("LADOS GUARDADOS")

opc=0
max=5
while(opc!=max):
    print("######## MENU 3 #########")
    print("#####  CANTIDAD DE: #####")
    print("#-----------------------#")
    print("# 1.Lados Cuadrilatero  #")
    print("# 2.Lados de Triangulo  #")
    print("# 3.Lados de un pentago #")
    print("# 4.Lados de octagono   #")
    print("# 5.Salir del Menu ######")

    opc=libreria.pedir_numero("Ingrese opcion:",1,5)
    if(opc==1):
        cuadrilatero()
    if(opc==2):
        triangulo()
    if(opc==3):
        pentagono()
    if(opc==4):
        octagono()
print("FIN DE PROGRAMA ")