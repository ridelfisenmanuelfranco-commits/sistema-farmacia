# =======================================================================================
#                               GESTION DE CLIENTES
# =======================================================================================
from utilidades import limpiar_consola
from persistencia import guardar_clientes
from persistencia import cargar_clientes
# =======================================================================================
#                                       DATOS
# =======================================================================================
clientes = cargar_clientes()
contador_clientes = len(clientes) + 1

# =======================================================================================
#                                MENU DEL SISTEMA
# =======================================================================================
def mostrar_menu():
    print("""
    ====================================
                CLIENTES
    ====================================
    1. Registrar cliente
    2. Mostrar clientes
    3. Buscar cliente
    4. Actualizar cliente
    5. Eliminar cliente
    6. Volver
    ====================================
    """)


# =======================================================================================
#                               OBTENER CODIGO DEL CLIENTE
# =======================================================================================
def obtener_codigo_cliente():
    global contador_clientes

    codigo_cliente = f'CLI-{contador_clientes:03}'
    contador_clientes += 1

    return codigo_cliente
# =======================================================================================
#                                OBTENER DATO
# =======================================================================================
def obtener_texto(prompt):
    while True:
        dato = input(prompt).strip().title()

        if dato == 'Salir':
            return None
        
        if dato == "":
            print('\n[ Nombre del cliente invalido. ]\n')
            continue

        return dato

# =======================================================================================
#                               OBTENER TELEFONO DEL CLIENTE
# =======================================================================================
def obtener_telefono_cliente():
    while True:
        
        telefono_cliente = input('Telefono del cliente: ').strip()

        if not telefono_cliente.isdigit():
            print('\n[ Telefono invalido. ]\n')
            continue

        if len(str(telefono_cliente)) != 10:
            print('\n[ Numero de telefono invalido. ]\n')
            continue
        
        if str(telefono_cliente)[:3] not in ['809', '829', '849']:
            print('\n[ Numero de telefono invalido. ]\n')
            continue
        
        telefono_cliente = f'({telefono_cliente[:3]}) {telefono_cliente[3:6]} {telefono_cliente[6:]}'
        return telefono_cliente
    

# =======================================================================================
#                                     CREAR CLIENTE      
# =======================================================================================
def crear_cliente(codigo_cliente, nombre_cliente, telefono_cliente):
    return {
        'Codigo': codigo_cliente,
        'Nombre': nombre_cliente,
        'Telefono': telefono_cliente
    }


# =======================================================================================
#                                   REGISTRAR CLIENTE
# =======================================================================================
def registrar_cliente():
    existe = False

    codigo_cliente = obtener_codigo_cliente()
    nombre_cliente = obtener_texto('Ingrese el nombre del cliente: ')
    
    if nombre_cliente is None:
        return
    
    for cliente in clientes:
        if cliente['Nombre'] == nombre_cliente:
            existe = True
            break

    if existe:
        print('\nEl cliente ya existe.\n')
        return
    
    telefono_cliente = obtener_telefono_cliente()

    for cliente in clientes:
        if cliente['Telefono'] == telefono_cliente:
            print('\nEl telefono ya existe.\n')
            return
        
    cliente = crear_cliente(codigo_cliente,
                            nombre_cliente,
                            telefono_cliente)

    clientes.append(cliente)
    guardar_clientes(clientes)

    print('\nCliente registrado exitosamente.\n')
# =======================================================================================
#                                    MOSTRAR CLIENTE   
# =======================================================================================
def mostrar_cliente(i, cliente):
    print(f'''
    =========================================
    {i+1}          CLIENTE
    =========================================
    Codigo      : {cliente['Codigo']}
    Nombre      : {cliente['Nombre']}
    Telefono    : {cliente['Telefono']}
    =========================================
    ''')
# =======================================================================================
#                                    MOSTRAR CLIENTES     
# =======================================================================================
def mostrar_clientes():
    if clientes:
        for i, cliente in enumerate(clientes):
            mostrar_cliente(i, cliente)

        print(f'\nTotal de clientes: {len(clientes)}\n')
        
    else:
        print('\nNo hay clientes registrados')

# =======================================================================================
#                                    BUSCAR CLIENTES POR CODIGO 
# =======================================================================================
def buscar_por_codigo(codigo):
    for i, cliente in enumerate(clientes):
        if cliente['Codigo'] == codigo:
            return i, cliente
            
    return None, None
    
# =======================================================================================
#                                    BUSCAR CLIENTES      
# =======================================================================================
def buscar_cliente():
    codigo_cliente_buscado = input('Codigo del cliente: ').strip().upper()
    i, cliente = buscar_por_codigo(codigo_cliente_buscado)
    
    if cliente:
        mostrar_cliente(i, cliente)
        
    else:
        print('\n[ Cliente no encontrado. ]\n')
    

# =======================================================================================
#                                   ACTUALIZAR CLIENTES            
# =======================================================================================
def actualizar_cliente():
    codigo_cliente_buscado = input('Codigo del cliente: ').strip().upper()
    i, cliente = buscar_por_codigo(codigo_cliente_buscado)
    
    if cliente:
        mostrar_cliente(i, cliente)
        
        cliente['Telefono'] = obtener_telefono_cliente()
        actualizar = input('Esta seguro que desea actualizar el cliente (si / no): ').strip().lower()
        if actualizar == 'si':
            guardar_clientes(clientes)
            print('\nCliente actualizado correctamente.\n')
            return
        elif actualizar == 'no':
            print('\n[ El cliente no ha sido actualizado. ]\n')
            return 
        else:
            print('\n[ Opcion invalida. ]\n')
    else:
        print('\nNo hay clientes registrados.\n')

# =======================================================================================
#                                     ELIMINAR CLIENTE
# =======================================================================================
def eliminar_cliente():
    codigo_cliente_buscado = input('Codigo del cliente: ').strip().upper()
    i, cliente = buscar_por_codigo(codigo_cliente_buscado)
    
    if cliente:
        print('\nCliente encontrado.\n')
        mostrar_cliente(i, cliente)
        eliminar = input('Esta seguro que desea eliminar el cliente (si / no): ').strip().lower()
        if eliminar == 'si':
            
            clientes.remove(cliente)
            guardar_clientes(clientes)
            print('\nCliente eliminado correctamente.\n')
            return
        elif eliminar == 'no':
            print('\n[ El cliente no ha sido eliminado. ]\n')
    
    else:
        print('\nCliente no encontrado.\n')

# ==============================================================================================
#                                       SISTEMA PRINCIPAL
# ==============================================================================================
def menu_clientes():
    while True:
        mostrar_menu()

        try:
            opcion = int(input('Elije una opcion: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue
        
        limpiar_consola()

        if opcion == 1:
            registrar_cliente()

        elif opcion == 2:
            mostrar_clientes()

        elif opcion == 3:
            buscar_cliente()

        elif opcion == 4:
            actualizar_cliente()

        elif opcion == 5:
            eliminar_cliente()

        elif opcion == 6:
            print('\nVolviendo al menu principal.\n')
            break
        else:
            print('\nOpcion invalida.\n')