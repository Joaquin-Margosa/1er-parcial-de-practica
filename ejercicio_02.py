"""Escribe un programa que calcule el área y el perímetro de un cuadrado y muestre los resultados (indicando cuál es cuál) por pantalla."""

lado=int(input("ingrese el valor de uno de los lados del cuadrado: "))
area= lado*lado #para obtener el area del cuadrado multiplicamos dos de sus lados.
perimetro= lado*4 #para obtener el perimetro del cuadrado multiplicacamos el valor de uno de sus lados por 4.
print("el area del cuadrado es:", area , "cm²")
print("el perimetro del cuadrado es:", perimetro , "cm")