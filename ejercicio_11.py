"""Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
a. Si es número par o impar
b. Cuanto es la suma total de todos los números mostrados
c. Cuanto es la suma total de todos los números pares mostrados
d. Cuanto es la suma total de todos los números impares mostrados"""

numeros= 1 
suma_de_todos_los_numeros= 0
suma_de_los_pares= 0
suma_de_los_impares= 0

while numeros <= 10: #Mostramos los números del 1 al 10.
    print(numeros)
    suma_de_todos_los_numeros+=numeros #Realizamos una suma de todos los números.
    
    if numeros %2==0: #Si el número es divisible por 2 significa que es par.
        print("Es par")
        suma_de_los_pares+=numeros #Realizamos una suma de todos los números pares.
    else: #si no es divisible por 2 significa que el número es impar.
        print("Es impar")
        suma_de_los_impares+=numeros #Realizamos una suma de todos los números impares.
    numeros+=1

#Mostramos en pantalla todos los resultados.
print("El resultado de la suma de todos los números es:", suma_de_todos_los_numeros)
print("La suma de todos los numeros pares es:", suma_de_los_pares)
print("La suma de todos los numeros impares es:", suma_de_los_impares)