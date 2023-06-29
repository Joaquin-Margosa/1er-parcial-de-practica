"""Escribe un programa que calcule el promedio general de una clase"""

cantidad_de_alumnos=int(input("Ingrese la cantidad de alumnos: ")) #Le pedimos al usuario que ingrese el número de alumnos.
notas= 1 #Contamos las notas dependiendo del número de alumnos ingresado.
acum= 0
while notas <= cantidad_de_alumnos: 
    nota_alumno=int(input("Ingrese la nota de un alumno: "))
    notas+=1
    acum= acum+nota_alumno #Sumamos las notas de todos los alumnos.
    promedio= acum/cantidad_de_alumnos #El promedio será igual a la división del resultado de la suma de las notas y la cantidad de notas.
print("el promedio general de la clase es:", promedio)