#5° Ejercicio
import libreria

def a_recto():
    input("Ingrese numero de angulo:")
    print("Numero de angulo guardado ")

def a_llano():
    input("Ingrese numero de angulo:")
    print("Numero de angulo guardado")

def a_vuelta():
    input("Ingrese nuero de angulo:")
    print("Numero de angulo guardado")

opc=0
max=4

while(opc!=max):
    print("####### MENU 5 #######")
    print("## VALOR DE ANGULOS ##")
    print("#--------------------#")
    print("# 1.Angulo recto     #")
    print("# 2.Angulo Llano     #")
    print("# 3.Angulo de vuelta #")
    print("# 4.Salir del menu   #")

    opc=libreria.pedir_numero("Ingrese opcion:",1,4)
    if(opc==1):
        a_recto()
    if(opc==2):
        a_llano()
    if(opc==3):
        a_vuelta()

print("FIN DEL PROGRAMA")