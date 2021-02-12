def numPerfectoProc(num):
    cont = 0
    for n in range(num):
        cont += n
        if cont >= num:
            break
    if cont == num:
        print("Perfecto: " + num.__str__())
    else:
        print("Imperfecto: "+ num.__str__())
def numPerfectoFunc(num):
    cont = 0
    for n in range(num):
        cont += n
        if cont >= num:
            break
    if cont == num:
        return True
    else:
        return False

##Para escribir los primeros 4 números perfectos basta con un bucle y un contador
contPerfectos = 0
REQ_PERFECTOS = 10
contLlamada = 1
res = ""
while (contPerfectos != REQ_PERFECTOS):
    if numPerfectoFunc(contLlamada):
        contPerfectos += 1
        res += contLlamada.__str__() + " - "
    contLlamada += 1
print(res[:-3])