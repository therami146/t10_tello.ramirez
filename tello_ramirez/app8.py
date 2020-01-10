#8° Ejercicio
import libreria

def arquitectura():
    input("Ingrese nombre de la primera escuela:")
    print("NOMBRE GUARDADO")

def civil():
    input("Ingrese nombre de la segunda escuela:")
    print("NOMBRE GUARDADO")

def informatica():
    input("Ingrese nombre de la tercera escuela:")
    print("NOMBRE GUARDADO")


opc=0
max=4

while(opc!=max):
    print("######## MENU 8 ########")
    print("### ESCUELAS DE FIME ###")
    print("#----------------------#")
    print("# 1.Primera escuela    #")
    print("# 2.Segunda escuela    #")
    print("# 3.Tercera escuela    #")
    print("# 4.Salir de menu  #####")

    opc=libreria.pedir_numero("Ingrese opcion:",1,4)
    if(opc==1):
        arquitectura()
    if(opc==2):
        civil()
    if(opc==3):
        informatica()

print("FIN DEL PROGRAMA ")
