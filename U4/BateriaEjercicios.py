# Suma a un número de veces igual a b

def misterio(a, b):
   if ( b == 1 ):
       return a
   else:
       return a + misterio(a, b-1)

