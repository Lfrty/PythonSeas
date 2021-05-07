import re
import datetime

# Variables compartidas en funciones _MENU es constante
_MENU = '+-------- Menú de opciones --------+\n\t(1) Añadir cliente\n\t(2) Eliminar cliente\n\t(3) Mostrar cliente\n\t(4) Listar clientes\n\t(5) Listar clientes preferentes\n\t(6) Terminar\nElige una opción:'
listaClientes = {}
opcion = ''
datoOk = False

# Para no repetir en cada función
def lenClientes():
    if(listaClientes == {}):
        print ('No hay clientes en la base de datos')
        return False
    return True


def testDato(patron, dni):
    datoOk = False
    if (re.match(patron, dni)):            
        datoOk = True
    return datoOk

def testFecha(patron, fecha):
    datoOk = False
    # Almaceno la fecha sin comillas
    fechaVar = fecha[1:len(fecha)-1]
    if(re.match(patron, fecha)):        
        try:
            # Convierto a fecha para comprobar si existe la fecha indicada, por ejemplo 31/04/2021 no sería válida
            datetime.datetime.strptime(fechaVar, '%d/%m/%Y')
            datoOk=True
        except:
            datoOk=False
    return datoOk
    
def anyadir():
    # Constantes con el patrón requerido para los datos
    PATTERN_DNI = '[0-9]{8}[a-zA-Z]'
    PATTERN_TELF = '[0-9]{9}'
    PATTERN_EMAIL = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    PATTERN_VIP = '[Y|N|S]'
    PATTERN_FECHA = "'[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}'"

    dni = input('Introduce dni del cliente: ')
    # Compruebo que DNI tenga la longitud correcta, tenga 8 letras y una letra (en testDni)
    while(not testDato(PATTERN_DNI, dni)):
        dni = input('Error, el dni debe contener 8 números y una letra (ej: 00523821F): ')
    # apellidos, nombre y dirección no requieren comprobación
    apellidosNombre = input('Introduce los apellidos y el nombre del cliente: ')
    direccion = input('Introduce la dirección del cliente: ')
    telefono = input('Introduce el teléfono del cliente: ')
    # Verifico que la longitud de teléfono sea de 9 dígitos y en su función de Test que sean solo números decimales
    while(not testDato(PATTERN_TELF, telefono)):
        telefono = input('Error, el teléfono debe de 9 dígitos(sin separación) (ej: 346071234): ')
    email = input('Introduce el correo electrónico del cliente: ')
    # Controlo que el email contenga un @ y acabe en .com o .es
    while(not testDato(PATTERN_EMAIL, email)):
        email = input('Correo electrónico no válido, debe incluir @ y . "ejemplo@hotmail.com": ')
    # Admito una s o una n, aunque sea en minúsculas la trasnforma en mayusculas
    vip = input('¿Es un cliente preferente (S/N)?: ').upper()
    while(not testDato(PATTERN_VIP, vip)):
        vip = input('Error, introduzca solo 1 carácter (S/N)?: ').upper()
    fechaOp = input('Introduce la fecha de la operación entre comillas: ')
    while(not testFecha(PATTERN_FECHA, fechaOp)):
        fechaOp = input('Error, introduzca una fecha válida entre comillas simples y sus valores entre / (\'01/01/2021\'): ')
    # Almaceno en el diccionario
    cliente = {'nombre':apellidosNombre, 'direccion':direccion, 'telefono':telefono, 'email':email,'fecha_operacion':fechaOp, 'preferente':vip}
    listaClientes[dni] = cliente
    print('¡Cliente añadido!')

# Estas funciones requieren una lista de clientes, si está vacía se omite mostrar o buscar
def eliminar():
    if (lenClientes()):
        dni = input('Introduce dni del cliente: ')
        if dni in listaClientes:
            print('Cliente con dni:' + listaClientes[dni] + ' eliminado')
            del listaClientes[dni]
        else:
            print('No existe el cliente con el dni ', dni)

def mostrarCliente():
    if (lenClientes()):
        dni = input('Introduce dni del cliente: ')
        if dni in listaClientes:
            print('DNI:', dni)
            for key, value in listaClientes[dni].items():
                print(key.title() + ':', value)
        else:
            print('No existe el cliente con el dni', dni)

def mostrarClientes():
    if (lenClientes()):
        print('Lista de clientes:\n')
        for key, value in listaClientes.items():
            print(key, value['nombre'])

def mostrarClientesVip():
    if (lenClientes()):
        print('Lista de clientes preferentes:')
        for key, value in listaClientes.items():
            if value['preferente']:
                print(key, value['nombre'])        

# Mientras no se seleccione la opción 6 el programa no sale
# Para evitar usar excepciones toma la opción como un string
while opcion != '6':
    if opcion == '1':
        anyadir()
    elif opcion == '2':
        eliminar()
    elif opcion == '3':
       mostrarCliente()
    elif opcion == '4':
        mostrarClientes()
    elif opcion == '5':
        mostrarClientesVip()
    else:
        print('Introduzca una de las opciones del menú (1-6)')
    # La vconstante Menú es una plantilla declarada en el top
    opcion = input(_MENU)
