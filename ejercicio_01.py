"""Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el año de nacimiento"""

year=int(input("Ingrese el año de su nacimiento: ")) #le pedimos al usuario que ingrese el año de su nacimiento para conocer su edad.
edad=2023-year #para ello realizamos una resta entre el año actual y el año de su nacimiento.
print("Usted tiene", edad , "años de edad")