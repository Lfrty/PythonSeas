def maxInt (arrayInt):
    var = arrayInt[0]
    res = 0
    for i in arrayInt:
        if (i>var):
            res = i
    return res

num = 0
numsEnteros = []
print('Introduce números y te mostraré el mayor. ENTER para terminar')
while(num!=''):
    num = input()
    if(num!=''):
        print('Añadido ' + num)
        numsEnteros.append(num)

print('El número mayor es: ' + maxInt(numsEnteros))
    


