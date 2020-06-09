"""Vamos a crear un programa que lea varios números,
los que el usuario quiera, los añada a una lista y después
los meta en un conjunto donde se mostrarán sin repetirse"""

totalNumeros=0
numActual=0
lista = list()
conjunto = set() #Variables que usaremos

totalNumeros= int(input("¿Cuántos números vas a introducir?: "))

for i in range(totalNumeros): #Hacemos totalNumeros un rango para ser interpretado como una tupla y que lo acepte for
    numActual = int(input("Introduce un número entero: "))
    lista.append(numActual) #Leemos el número lo parseamos a entero y lo guardamos en lista

conjunto = set(lista) #NOTA: al pasar de una lista a un conjunto estos no se cambian a menos que "parsees" un conjunto
print("Los números que has introducido son: ")
print(lista)
print("Los valores son: ")
print(conjunto)
