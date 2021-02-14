_MENU = '+-------- Menú de opciones --------+\n'+chr(127)+'\t(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:'
clients = {}
option = ''

def anyadir():
    nif = input('Introduce NIF del cliente: ')
    name = input('Introduce el nombre del cliente: ')
    address = input('Introduce la dirección del cliente: ')
    phone = input('Introduce el teléfono del cliente: ')
    email = input('Introduce el correo electrónico del cliente: ')
    vip = input('¿Es un cliente preferente (S/N)? ')
    client = {'nombre':name, 'dirección':address, 'teléfono':phone, 'email':email, 'preferente':vip=='S'}
    clients[nif] = client

def eliminar():
    nif = input('Introduce NIF del cliente: ')
    if nif in clients:
        del clients[nif]
    else:
        print('No existe el cliente con el nif', nif)

def mostrarCliente():
    nif = input('Introduce NIF del cliente: ')
    if nif in clients:
        print('NIF:', nif)
        for key, value in clients[nif].items():
            print(key.title() + ':', value)
    else:
        print('No existe el cliente con el nif', nif)

def mostrarClientes():
    print('Lista de clientes')
    for key, value in clients.items():
        print(key, value['nombre'])

def mostrarClientesVip():
    print('Lista de clientes preferentes')
    for key, value in clients.items():
        if value['preferente']:
            print(key, value['nombre'])

while option != '6':
    if option == '1':
        anyadir()
    if option == '2':
        eliminar()
    if option == '3':
       mostrarCliente()
    if option == '4':
        mostrarClientes()
    if option == '5':
        mostrarClientesVip()
    option = input(_MENU)




