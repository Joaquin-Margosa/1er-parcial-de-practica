"""Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar)."""

dolares= int(input("ingrese la cantidad de dolares a convertir: ")) #Deseamos convertir dolares a pesos, y para ello pedimos al usuario que ingrese la cantidad de dólares que desea convertir.
valor_del_dolar= int(input("ingrese el valor actual del dolar: ")) #Ahora le pedimos que ingrese el valor actual del dólar.
equivalencia= dolares * valor_del_dolar #Para la conversión realizamos una multiplicación, cantidad de dólares por el valor actual del dólar.
print("la equivalencia a pesos es" , equivalencia) #Obtenemos el valor en pesos.