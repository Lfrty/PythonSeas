x = int(input("Cuántos términos quieres?: "))
v1, v2 = 1, 1
res = 0
cont = 0
salida = "1 - 1 - "

if x == 1:
    print("1")
    exit(0)
elif x == 2:
    print("1-1")
    exit(0)
elif x == 0:
    exit(0)
else:
    cont = 2

while cont < x:
    cont += 1
    res = v1 + v2  # Almaceno la suma
    v1 = v2  # Traspaso el valor anterior al anterior correspondiente
    v2 = res  # Almaceno el resultado para la siguiente suma
    salida += str(res) + " - "
print(salida[:-3])  # Excluyo los 2 espacios y el guión final
