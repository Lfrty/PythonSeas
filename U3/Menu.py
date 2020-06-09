#Ejercicio que explora opciones de Menu
x=0
res=""
while True:
    x=int(input("Selecciona una opción: "))
    if(x==1):
        res="Acceso a opción 1"
        break
    elif(x==2):
        res="Acceso a opción 2"
        break
    elif(x==3):
        res="Acceso a opción 3"
        break
    else:
        print("Por favor, selecciona una opción del 1 al 3")
        continue
print(res)
