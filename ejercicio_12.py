"""Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no hacerlo más, y muestre, al final, un promedio de las edades ingreasdas y el total de personas ingresadas"""

#Este programa le permite al usuario ingresar edades de personas ilimitadas veces, hasta que decida no hacerlo mas.
cont_edades= 0 
acum_edades= 0 
decision= 1 #Variable booleana que nos permite ingresar dos valores posibles.
while decision==1: 
    edades=int(input("Ingrese la edad: "))
    cont_edades+=1 
    acum_edades=acum_edades+edades 
    decision=int(input("¿Desea seguir ingresando edades? Si=1 No=0 ")) #Con dos valores posibles, el usuario puede decidir escribiendo 1 si desea seguir y 0 para decirle al programa que ya no quiere seguir.
    if decision==0: #Si su decisión es 0, el programa procede a calcular el promedio y el total de edades ingresadas. 
        promedio_edades=acum_edades/cont_edades
        print("Promedio de las edades ingresadas:", promedio_edades , "\n" "Total de personas ingresadas:", cont_edades)
    elif decision>1:
        print("Solo puede escribir los números 1 o 0")