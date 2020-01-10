#4° ejercicio
import libreria

def episodio_1():
    input("Ingrese el episodio:")
    print("NUMERO DE EPISODIO GUARDADO")
def episodio_2():
    input("Ingrese el episodio:")
    print("NUMERO DE EPISODIO GUARDADO")
def episodio_3():
    input("Ingrese el episodio:")
    print("NUMERO DE EPISODIO GUARDADO")
def episodio_4():
    input("Ingrese el episodio:")
    print("NUMERO DE EPISODIO GUARDADO")

opc=0
max=5

while(opc!=max):
    print("########  MENU 4    #########")
    print("## EPISODIOS DE STAR WARS  ##")
    print("#---------------------------#")
    print("# 1.la amenaza fantasma     #")
    print("# 2.El ataque de los clones #")
    print("# 3.La venganza de los sith #")
    print("# 4.Una nueva esperanza     #")
    print("# 5.SALIR             #######")
    opc=libreria.pedir_numero("ingrese opcion:",1,5)

    if(opc==1):
        episodio_1()
    if(opc==2):
        episodio_2()
    if(opc==3):
        episodio_3()
    if(opc==4):
        episodio_4()

print("FIN DEL PROGRAMA")