"""Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales, indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6)."""

#Le pedimos al usuario que ingrese tres notas 
nota1=int(input("Ingrese la nota del primer parcial: "))
nota2=int(input("Ingrese la nota del segundo parcial: "))
nota3=int(input("Ingrese la nota del tercer parcial: "))
prom=nota1+nota2+nota3/3 #Para obtener el promedio sumamos las tres notas y las dividimos por 3.
if prom>6: #Si el promedio es mayor a 6 significa que el alumno aprobó la materia y no debe recursarla, y si es menor a 6 deberá recursarla.
    print("El alumno aprobó la materia y no debe recursarla")
else: 
    print("El alumno no aprobó y debe recursar la materia")