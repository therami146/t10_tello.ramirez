#6° Ejercicio
import libreria

def facfym():
    input("Ingrese nombre de facultad:")
    print("NOMBRE DE FACULTAD GUARDADO ")

def fmv():
    input("Ingrese nombre de facultad:")
    print("NOMBRE DE FACULTAD GUARDADO ")

def fime():
    input("Ingrese nombre de facultad:")
    print("NOMBRE DE FACULTAD GUARDADO ")

def facshe():
    input("Ingrese nombre de facultad:")
    print("NOMBRE DE FACULTAD GUARDADO ")

opc=0
max=5

while(opc!=max):
    print("######## MENU 7 ########")
    print("### FACULTADES UNPRG ###")
    print("#----------------------#")
    print("# 1.Nombre de FACFYM   #")
    print("# 2.Nombre de FMV      #")
    print("# 3.Nombre de FIME     #")
    print("# 4.Nombre de FACSHE   #")
    print("# 5.Salir del menu  ####")

    opc=libreria.pedir_numero("Ingrese opcion:",1,5)
    if(opc==1):
        facfym()
    if(opc==2):
        fmv()
    if(opc==3):
        fime()
    if(opc==4):
        facshe()

print("FIN DEL PROGRAMA")

