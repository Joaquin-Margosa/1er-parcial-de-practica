"""Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de horas, escribe un programa que calcule el descuento anual a realizarse, considerando:
a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5
b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3
c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1
d. El programa debe mostrar el salario anual bruto, el monto anual de bonificaciones, el monto anual a descontarse y las horas trabajadas en todo el año."""

horas=int(input("Ingrese la cantidad de horas trabajadas: "))
if horas>192:
    print("el valor es incorrecto")
elif horas>120:
    multiplicacion= horas * 1500
    bonificacion= multiplicacion * 0.18
    print("Sueldo bruto:", multiplicacion, "\n" "Monto a bonificar:", bonificacion , "\n" "Sueldo neto:", multiplicacion+bonificacion)
elif horas>80 and horas<120:
    multiplicacion= horas * 1300 
    bonificacion= multiplicacion * 0.15
    print("Sueldo bruto:", multiplicacion, "\n" "Monto a bonificar:" , bonificacion , "\n" "Sueldo neto:", multiplicacion+bonificacion)
elif horas<80:
    multiplicacion = horas*1100
    bonificacion= multiplicacion * 0.13
    print("Sueldo bruto:", multiplicacion, "\n" "Monto a bonificar:" , bonificacion , "\n" "Sueldo neto:", "Sueldo neto:", multiplicacion+multiplicacion)

#En este caso, el programa va a calcular el sueldo anual, monto anual a bonificar, monto anual a descontar y las horas trabajadas durante todo el año.

sueldo_anual= multiplicacion * 12 #El sueldo anual será igual a la multiplicación del sueldo bruto por 12 meses.
bonificacion_anual= bonificacion * 12 #El monto anual a bonificar será igual a la multiplicación del valor de la bonificación por 12 meses.
horas_anuales= horas * 12 #Las horas trabajadas en todo el año será igual a la multiplicación de las horas trabajadas en un mes por 12 meses.
if sueldo_anual>2000000: #Si el valor del sueldo anual supera un cierto limite, se realizará el descuento anual multiplicando el valor del sueldo anual por el valor del porcentaje.
    descuento= sueldo_anual * 0.05
elif sueldo_anual>1000000 and sueldo_anual<2000000:
    descuento= sueldo_anual * 0.03
elif sueldo_anual<1000000:
    descuento= sueldo_anual * 0.01
print("Sueldo bruto anual:", sueldo_anual , "\n" "Monto anual a descontar:" , descuento , "\n" "Monto anual a bonificar", bonificacion_anual , "\n" "Durante el año trabajó" , horas_anuales , "horas")