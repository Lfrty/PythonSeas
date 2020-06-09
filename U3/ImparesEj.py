x=1
salida = ""
while x <= 19:
    if x % 2 != 0:
        salida += str(x) + " - "
    x+=1
print(salida[:-3])
