"""Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre por pantalla el resultado, considerando lo siguiente: 
Si trabajo más de 120hs por mes, la hora tiene un valor de $1500
Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300
Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100"""

horas=int(input("Ingrese la cantidad de horas trabajadas: ")) #Dependiendo de la cantidad de horas trabajadas que el usuario ingrese, el sueldo del empleado será calculado en base a ello.
if horas>192: #Si trabajó más de un cierto limite de horas por mes, el programa va a calcular el sueldo multiplicando la cantidad de horas ingresadas por el valor de la hora.
    print("El valor es incorrecto") #Si la cantidad de horas ingresadas excede el maximo de horas, el programa indicará que el valor ingresado es incorrecto.
elif horas>120: 
    sueldo= horas * 1500
    print("El empleado va a cobrar $", sueldo) #El resultado de la multiplicacion será el sueldo del empleado.
elif horas>80 and horas<120:
    sueldo= horas * 1300
    print("El empleado va a cobrar $", sueldo)
elif horas<80:
    sueldo= horas*1100
    print("El empleado va a cobrar $", sueldo)