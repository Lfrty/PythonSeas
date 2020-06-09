"""Vamos a crear una lista de números, esta estará desordenada
pero lo iremos añadiendo a otra lista para ordenarla de mayor a menor"""

#Primero las variables que necesitaremos
listaOrd = []
listaDesord = []
numActual = 0 # Numero a leer
numTotal = 0 # Total de números a introducir

numTotal = int(input("¿Cuántos números introducirás?: "))

for i in range(numTotal):
    numActual = int(input("Introduce un número entero: "))
    listaDesord.append(numActual)

print("Tu lista como la escribiste: ") #Escribimos antes el resultado para hacer uso de la variable listaDesord
print(listaDesord)

#Ahora la ordenaremos al revés, haremos uso de la variable numActual para coger el máximo y añadirla
for i in range(numTotal):
    numActual = max(listaDesord)
    listaOrd.append(numActual)
    listaDesord.remove(numActual)

print("Tu lista ordenada de MAYOR a MENOR: ")
print(listaOrd)