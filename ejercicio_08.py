"""Escribe un programa que solicite y muestre por pantalla el nombre, apellido y edad de 5 personas"""

personas= 1 #Utilizamos un contador para contar la cantidad de personas que ingresan sus datos.
while personas <= 5: #En este caso, serán 5 personas las que ingresarán sus datos.
    print("Datos de la persona N°", personas)
    nombre=str(input("Ingrese su nombre: "))
    apellido=str(input("Ingrese su apellido: "))
    edad=int(input("Ingrese su edad: "))
    personas=personas+1
    #Muestra por pantalla los datos de cada persona.
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Edad:", edad , "años")
    
