"""Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto (bruto + bonif), considerando:
Si trabajo más de 120hs, la bonificación es de %18
Si trabajo entre 80 y 120 horas, la bonificación es de %15
Si trabajo menos de 80 horas, la bonificación es de %13"""

horas=int(input("Ingrese la cantidad de horas trabajadas: ")) #Del punto anterior, este programa va a calcular el sueldo bruto, el monto a bonificar y el sueldo neto.
if horas>192:
    print("El valor es incorrecto")
elif horas>120:
    multiplicacion= horas * 1500 #La cantidad de horas trabajadas en el mes por el valor de la hora será igual al sueldo bruto.
    bonificacion= multiplicacion * 0.18 #El monto a bonificar será igual a la multiplicación del sueldo bruto por el valor del porcentaje de bonificación. 
    print("Sueldo bruto:", multiplicacion , "\n" "Monto a bonificar:", bonificacion , "\n" "Sueldo neto:", multiplicacion+bonificacion) #El sueldo neto será igual a la suma del sueldo bruto mas la bonificación.
elif horas>80 and horas<120:
    multiplicacion= horas * 1300 
    bonificacion= multiplicacion * 0.15
    print("Sueldo bruto:", multiplicacion, "\n" "Monto a bonificar:" , bonificacion , "\n" "Sueldo neto:", multiplicacion+bonificacion)
elif horas<80:
    multiplicacion = horas*1100
    bonificacion= multiplicacion * 0.13
    print("Sueldo bruto:", multiplicacion, "\n" "Monto a bonificar:" , bonificacion , "\n" "Sueldo neto:", multiplicacion+bonificacion)