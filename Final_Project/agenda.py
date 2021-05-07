#Módulos
from pathlib import Path
import re

_MENU = '_______ MENÚ ______\n1. Obtener un teléfono.\n2. Insertar un teléfono.\n3. Eliminar un teléfono.\n4. Salir \nInserta una opción:'
_PATTERN_OPTION = '[1-4]{1}'
_PATTERN_TELF_MOVIL = '(\+34|0034|34)?[ -]*(6|7)[ -]*([0-9][ -]*){8}'
_PATTERN_TELF_FIJO = '(\+34|0034|34)?[ -]*(8|9)[ -]*([0-9][ -]*){8}'
_FICHERO = 'agenda.txt'

class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return self.nombre.strip() + ',' + self.telefono.strip()

class Agenda:
    _PATTERN_NUMBER = '/[^0-9]/g'
    archivoVacio = ''
    agenda = []

    def verificar_cant_contactos(self):
        if(len(self.agenda)==0):
            self.archivoVacio=True
            print('Archivo sin contactos')

    # Comprueba si existe el fichero y devuelve un booleano, en caso de que no da la opción de crearlo
    def existe_fichero(self):
        encontrado = False
        try:
            fichero = open(_FICHERO, 'r')
            encontrado = True
            fichero.close()
        except:
            print('ERROR: No se encuentra el archivo')
            opcion=input('¿Crear nuevo fichero y añadirlo?: ')
            if(opcion == 's'):
                fichero = Path(_FICHERO)
                fichero.touch(exist_ok=True)
                print('¡Un nuevo archivo (agenda.txt) ha sido creado!')
                self.archivoVacio= True
                encontrado = True
            else:
                print('No se creó la agenda, sin la agenda no se pueden realizar las operaciones')
        return encontrado    

    # Copia el archivo entero en una lista
    def leer_agenda(self):
        # Vacío la agenda (lista) para no repetir nombres en casos de errores
        error=False
        self.agenda= []
        with open(_FICHERO, 'r') as fichero:
            lineas = fichero.readlines()
        fichero.close()
        for linea in lineas:
            try:
                nuevoContacto = Contacto(linea.split(',')[0], linea.split(',')[1])
                self.agenda.append(nuevoContacto)
            except:
                error = True
        if(error):
            print('Ha ocurrido un error al explorar el archivo, se procede a limpiar el mismo')
            self.grabar_agenda()
                    
        self.verificar_cant_contactos()
            
    # Comprueba si existe algún nombre y teléfono con los datos introducidos
    def obten_telefono(self, nombrePersona):
        resultado = []
        if (self.existe_fichero()):
            self.leer_agenda()
            for contacto in self.agenda:
                if(re.search(nombrePersona, contacto.nombre, re.IGNORECASE)):
                    resultado.append(contacto)
            if(len(resultado)>0):
                print('Hemos encontrado estos datos: ')
                for contacto in resultado:
                    self.imprime(contacto)
            else:
                print('No hemos encontrado ningún contacto relacionado')

    # Añade un contacto, de no existir propone crear uno nuevo
    def inserta_telefono(self, contacto):
        if(self.existe_fichero()):
            self.grabar(contacto, 'a') ## Manda a guardar el archivo 
            self.archivoVacio = False
        else:
            opcion=input('¿Crear nuevo fichero y añadirlo?')
            if(opcion == 's'):
                self.grabar(contacto, 'w') # Manda a guardar el archivo y crearlo
                self.archivoVacio=False # Muestra que el archivo ya no está vacío
            else:
                print('No se creó el archivo. El contacto no fue añadido')

    # Elimina un contacto
    def elimina_telefono(self, nombre):
        contNombresIguales = 0
        listaNombres = []
        # Sí no está vacío entra
        if (not self.archivoVacio):
            self.obten_telefono(nombre)
            nombreParaBorrar = input('Escribe exactamente el nombre si quieres eliminarlo definitivamente de tus contactos (Si está repetido podrás elegir cual): \n')
            for contacto in self.agenda: # Busca en la agenda exactamente el mismo nombre
                if(contacto.nombre == nombreParaBorrar):
                    contNombresIguales +=1 # Por si el nombre está repetido
                    listaNombres.append(contacto)
            if (contNombresIguales>1): # En caso de haber más de 1 mostrará los de nombre repetido
                for contacto in listaNombres:
                    print('vvvvvvvvvvvv\n')
                    print('Número: ' + str(listaNombres.index(contacto)+1) +'\n')#Muestra la info y un número empezando desde el 1
                    self.imprime(contacto)                    
                    print('^^^^^^^^^^^^')
                option = input('Introduce el número del contacto que deseas eliminar (0 para salir): ')
                while (True and option!=0): #Mientras no se inserte un dígito el bucle segirá funcionando, o se introduza q para salir
                    try:
                        option = int(option) # Trata de convertir a entero para poder entrar como index
                        break
                    except:
                        input('Debe ser un número de los indicados (0 para salir): ') # Sino reservo el 0 para salir                       
                if(option == 0):
                    print('Volviendo al menú...')
                    return
                try:
                    self.agenda.remove(listaNombres[int(option)-1]) #Elimina el contacto de agenda con el index de la lista creada con nombres repetidos
                    print('Contacto eliminado')
                    self.grabar_agenda() # De ser eliminado actualiza el archivo
                except:
                    print('Error, no se ha insertado un dígito de los especificados')
                    return
            elif(contNombresIguales == 1):
                self.agenda.remove(listaNombres[0])
                # Si era el último contacto marca el archivo vacío como True
                self.verificar_cant_contactos() # Compueba si está vacío el archivo y lo almacena
                print('Contacto eliminado')
                self.grabar_agenda()    # En base a la lista agenda crea un nuevo archivo con los datos eliminando el elegido
            else:     
                print('Contacto no encontrado')
        else:
            print('No se puede eliminar ningún contacto, no hay ninguno o el archivo ha sido eliminado')  

    # Añade un contacto al fichero
    def grabar(self,contacto, modo):        
        fichero = open(_FICHERO, modo)
        fichero.write(str(contacto) + '\n')
        fichero.close()
        print('Nuevo contacto añadido')
    
    # Machaca el anterior archivo y escribe de nuevo los datos sin contar con el eliminado
    def grabar_agenda(self):
        fichero = open(_FICHERO,'w')
        for contacto in self.agenda:
            fichero.write(str(contacto)+ '\n')
        fichero.close()
        print('Datos actualizados')
        # Vacío la agenda para que no se sobreescriban nombres
        self.agenda = []
    
    def imprime(self, contacto):
        print('+---------+\n|Nombre: ' + contacto.nombre)
        print('|---------+\n|Telefono: ' + contacto.telefono + '+---------+\n')

# Tomo los datos para mandarlos a insertar
def tomar_datos():    
    nombre = input('Introduce el nombre: ') #Existiendo comas en el nombre no dejará insertarlo
    while (',' in nombre):
        nombre = input('No se admiten comas (,) en el nombre por favor introduce otro: ')
    telefono = input('Introduce el teléfono: ')
    while (not re.match(_PATTERN_TELF_FIJO, telefono) and not re.match(_PATTERN_TELF_MOVIL, telefono)):
        telefono = input('Introduce un número de teléfono válido en España (Ejemplos: 952-56-78-90 ó +34 660 87 65 99): ')

    return Contacto(nombre, telefono)

def menu():
    agenda = Agenda()
    opcion = ''
    agenda.existe_fichero();
    while(True):
        opcion = input(_MENU)
        if(re.match(_PATTERN_OPTION, opcion)):
            if (opcion == '1'):
                if(not agenda.archivoVacio and agenda.existe_fichero()):
                    agenda.obten_telefono(input('Introduce el nombre del contacto que quieres ver: '))
                else:
                    print('Agenda vacía o archivo no encontrado, introduce un nuevo contacto para empezar.')
            elif(opcion == '2'):
                agenda.inserta_telefono(tomar_datos())
            elif(opcion == '3'):
                if(not agenda.archivoVacio and agenda.existe_fichero()):
                    agenda.elimina_telefono(input('Introduce el nombre del contacto a eliminar: '))
                else:
                    print('Agenda vacía o archivo no encontrado, introduce un nuevo contacto para empezar.')
            elif(opcion == '4'):
                break
        else:
            print('Introduce una opción valida (1-4)')

menu()