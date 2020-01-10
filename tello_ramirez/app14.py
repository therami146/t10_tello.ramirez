#14° EJERCICIO
import libreria

def i3():
    print("PROCESADOR GAMA I3")
    contenido="SE INGRESO EL PROCESADOR"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")

def i5():
    print("PROCESADOR GAMA I5")
    contenido = "SE INGRESO EL PROCESADOR"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")

def i7():
    print("PROCESADOR GAMA I7")
    contenido = "SE INGRESO EL PROCESADOR"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")

def i9():
    print("PROCESADOR GAMA I9")
    contenido = "SE INGRESO EL PROCESADOR"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")

def intel():
    opc=0
    max=5
    while(opc!=max):
        print("############ SUBMENU ##########")
        print("# 1.I-core 3")
        print("# 2.I-core 5")
        print("# 3.I-core 7")
        print("# 4.I-core 9")
        print("# 5.SALIR DEL SUB MENU")
        opc=libreria.pedir_numero("Ingrese opcion:",1,5)

        if(opc==1):
            i3()

        if(opc==2):
            i5()

        if(opc==3):
            i7()

        if(opc==9):
            i9()

opc=0
max=2
while(opc!=max):
     print("########### MENU #################")
     print("# 1.PROCESADORES INTEL")
     print("# 2.SALIR DEL MENU")
     opc=libreria.pedir_numero("INGRESE OPCION:",1,2)

     if(opc==1):
         intel()

print("FIN DEL MENU")
