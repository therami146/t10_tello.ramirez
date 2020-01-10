#13° EJERCICIO
import libreria

def algebra():
    print("SE GUARDO CURSO DE ALGEBRA")
    contenido="SE INGRESO CURSO DE ALGEBRA"
    libreria.guardar_datos("inf.txt",contenido,"a")
    print("SE GUARDA LOS DATOS")

def fisica():
    print("SE GUARDO CURSO DE FISICA")
    contenido="SE INGRESO CURSO DE FISICA"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")
def historia():
    print("SE GUARDO CURSO DE HISTORIA")
    contenido="SE INGRESO CURSO DE HISTORIA"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")
def literatura():
    print("SE GUARDO CURSO DE LITERATURA")
    contenido="SE INGRESO CONTENIDO DE LITERATURA"
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("SE GUARDA LOS DATOS")
def matematicas():
    opc=0
    max=3
    while(opc!=max):
        print("######### SUBMENU 1 ############# ")
        print("# 1.ALGEBRA")
        print("# 2.FISICA")
        print("# 3.SALIR DEL SUBMENU")
        opc=libreria.pedir_numero("Ingrese opcion:",1,3)
        if(opc==1):
            algebra()
        if(opc==2):
            fisica
def letras():
    opc=0
    max=3
    while(opc!=max):
        print("############### SUB MENU 2 ########")
        print("# 1.HISTORIA")
        print("# 2.LITERATURA")
        print("# 3.SALIR DEL SUBMENU")
        opc=libreria.pedir_numero
        if(opc==1):
            historia()
        if(opc==2):
            literatura()

opc=0
max=3
while(opc!=max):
    print("########## SUB MENU 3 ############")
    print("# 1.CURSOS DE MATICAS #")
    print("# 2.CURSOS DE LETRAS  #")
    print("# 3. SALIR DEL MENU   #")

    opc=libreria.pedir_numero("Ingrese opcion:",1,3)
    if(opc==1):
        matematicas()

    if(opc==2):
        letras()

print("FIN DEL MENU CTM")