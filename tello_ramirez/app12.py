#12° EJERCICIO
import libreria

def campeon_fut():
    print("SE INGRESO CAMPEON DE FUT ")


def numero_fut():
    print("SE INGRESO SUB CAMPEON DEL MUNDIAL")

def campeones_vol():
    print("SE INGRESO CAMPEONAS DEL MUNDO")

def numero_vol():
    print("SE INGRESO SUB CAMPEON DE LA COPA AMERICA ")

def futbol():
    opc=0
    max=3

    while(opc!=max):
        print("###########  SUB MENU 1 ##########")
        print("# 1.FRANCIA CAMPEON 2018")
        print("# 2.CROACIA 2018")
        print("# 2.SALIR DEL SUBMENU")
        opc=libreria.pedir_numero("Ingrese opcion:",1,2)

        if(opc==1):
            campeon_fut()
        if(opc==2):
            numero_fut()

def voley():
    opc=0
    max=3
    while(opc!=max):
        print("########### SUB MENU 2 ##########")
        print("# 1.BRASIL CAMPEON 2019")
        print("# 2.PERU 2019")
        print("# 3.SALIR DEL SUBMENU")
        opc=libreria.pedir_numero("Ingrese opcion:",1,3)

        if(opc==1):
            campeones_vol()

        if(opc==2):
            numero_vol()
opc=0
max=3

while(opc!=max):
    print("################ MENU ##########")
    print("# 1.CAMPEON DEL MUNDIA 2018")
    print("# 2.CAMPEON DE LA COPA AMERICA 2019")
    print("# 3.SALIR DEL MENU")
    opc=libreria.pedir_numero("Ingrese una opcion:",1,3)

    if(opc==1):
        futbol()
    if(opc==2):
        voley()
print("SE TERMINO EL MENU ")