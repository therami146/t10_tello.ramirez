import libreria

def platano():
    print("SE INGRESO LA OPCION PLATANOS")
    contenido="SE INGRESO LA OPCION PLATANOS"  + "\n"
    libreria.guardar_datos("inf.txt",contenido,"a")
    print("SE GUARDA LOS DATOS")
def fresa():
    print("SE INGRESO LA OPCION FRESA")
    contenido="SE INGRESO LA OPCION FRESA" + "\n"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")
def manzana():
    print("SE INGRESO LA OPCION MANZANA")
    contenido="SE INGRESO LA OPCION MANZANA" + "\n"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")
def pepino():
    print("SE INGRESO LA OPCION PEPINO")
    contenido="SE INGRESO OPCION PEPINO"  + "\n"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")

def cebolla():
    print("SE INGRESO LA OPCION CEBOLLA")
    contenido="SE INGRESO OPCION CEBOLLA" + "\n"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")
def zanahoria():
    print("SE INGRESO LA OPCION ZANAHORIA")
    contenido="SE INGRESO OPCION ZANAHORIA" + "\n"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")

def frutas():
    opc=0
    max=4
    while(opc!=max):
        print("############ SUBMENU1 ###########")
        print("# 1.PATANO #")
        print("# 2.FRESA #")
        print("# 3.MANZANA #")
        print("# 4.SALIR DEL MENU #")
        opc=libreria.pedir_numero("Ingrese opcion:",1,4)

        if(opc==1):
            platano()

        if(opc==2):
            fresa()

        if(opc==3):
            manzana()

def verduras():
    opc=0
    max=4
    while(opc!=max):
        print("######## SUBMENU 2 #########")
        print("# 1.PEPINO #")
        print("# 2.CEBOLLA")
        print("# 3.ZANAHORIA")
        print("# 4.SALIR DEL MENU")

        opc=libreria.pedir_numero("Ingrese opcion:",1,4)
        if(opc==1):
            pepino()

        if(opc==2):
            cebolla()

        if(opc==3):
            zanahoria()


opc=0
max=3

while(opc!=max):
    print("########### MENU 1 ############")
    print("# 1.FRUTAS #")
    print("# 2.VERDURAS #")
    print("# 3.SALIR DEL MENU #")
    print("###############################")

    opc=libreria.pedir_numero("Ingrese opcion:",1,3)

    if(opc==1):
        frutas()

    if(opc==2):
        verduras()

print("FIN DEL PROGRAMA CTM")