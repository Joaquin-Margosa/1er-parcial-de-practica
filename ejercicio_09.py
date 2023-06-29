"""Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de personas ingresada por el usuario"""

#La cantidad de personas de las que desea mostrar sus datos por pantalla dependerá del número que usted ingrese.
cantidad_de_personas=int(input("Ingrese un número de personas de las que desea mostrar en pantalla sus datos: ")) 
contador = 1 #Nuevamente utilizamos un contador para contar la cantidad de personas. 
while contador <= cantidad_de_personas: 
    print("Persona N°", contador)
    nombre=str(input("Ingrese su nombre: "))
    apellido=str(input("Ingrese su apellido: "))
    edad=int(input("Ingrese su edad: "))
    #Datos de la cantidad personas ingresadas.
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Edad:", edad)
    contador=contador+1