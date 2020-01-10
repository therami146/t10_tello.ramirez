#2° Ejercicio
import libreria
def musica_p():
    input("Rey del pop:")
    print("DATO GUARDADO")

def musica_r():
    input("Ingrese sus años dorados:")
    print("SE INGRESO LOS AÑOS 90")

opc=0
max=3
while(opc!=max):
    print("####### MENU 2 ########")
    print("### Representantes: ###")
    print("#---------------------#")
    print("# 1.Musica Pop     ####")
    print("# 2.Musica Rock    ####")
    print("# 3.salir   ###########")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        musica_p()

    if(opc==2):
        musica_r()

print("FIN DEL PROGRAMA :) ")