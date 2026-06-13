# =======================================================================================
#                                GESTION DE VENTAS
# =======================================================================================
from utilidades import limpiar_consola
from gestion_cliente import clientes
from gestion_empleado import empleados
from gestion_medicamentos import medicamentos

# =======================================================================================
#                                           DATOS
# =======================================================================================
ventas = []
contador_ventas = 1

# =======================================================================================
#                                      MENU DE VENTAS
# =======================================================================================
def mostrar_menu_ventas():
    print('''
    ====================================
                VENTAS
    ====================================
    1. Registrar venta
    2. Mostrar ventas
    3. Buscar venta
    4. Eliminar venta
    5. Volver
    ====================================
    ''')


# =======================================================================================
#                               OBTENER CODIGO DE VENTA 
# =======================================================================================
def obtener_codigo_venta():
    global contador_ventas

    codigo_venta = f'VEN-{contador_ventas:03}'
    contador_ventas += 1

    return codigo_venta


# =======================================================================================
#                                OBTENER CLIENTE
# =======================================================================================
def obtener_cliente():
    while True:

        if not clientes:
            print('\nNo hay clientes registrados.\n')
            return None
        
        for i, cliente in enumerate(clientes):
            print(f'{i + 1}. {cliente["Nombre"]}')
        
        try:
            opcion = int(input('Seleccione el cliente: '))

        except ValueError:
            print('\nDato invalido\n')
            continue

        if 1 <= opcion <= len(clientes):
            return clientes[opcion -1]
        
        print('\nCliente invalido.\n')

# =======================================================================================
#                                OBTENER EMPLEADO
# =======================================================================================
def obtener_empleado():

    while True:

        if not empleados:
            print('\nNo hay empleado registrados.\n')
            return None
        
        for i, empleado in enumerate(empleados):
            print(f'{i + 1}. {empleado["Nombre"]}')
        
        try:
            opcion = int(input('Seleccione el empleado: '))

        except ValueError:
            print('\nDato invalido\n')
            continue

        if 1 <= opcion <= len(empleados):
            return empleados[opcion -1]
        
        print('\nEmpleado invalido.\n')


# =======================================================================================
#                                OBTENER MEDICAMENTO
# =======================================================================================
def obtener_medicamento():
    while True:
        
        if not medicamentos:
            print('\nNo hay medicamentos registrados.\n')
            return None
        
        for i, medicamento in enumerate(medicamentos):
            print(f'{i + 1}. {medicamento["Nombre"]}')

        try:
            opcion = int(input('Seleccione un medicamento: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue

        if 1 <= opcion <= len(medicamentos):
            return medicamentos[opcion - 1]
        
        print('\nMedicamento invalido.\n')

# =======================================================================================
#                                OBTENER CANTIDAD
# =======================================================================================
def obtener_cantidad_vender():
    while True:
        try:
            cantidad_a_vender = int(input('Cantidad a vender: '))
        
        except ValueError:
            print('\nDato invalido.\n')
            continue
            
        
        if cantidad_a_vender <= 0:
            print('\nCantidad invalida.\n')
            continue

        return cantidad_a_vender
    


# =======================================================================================
#                                       CREAR VENTA 
# =======================================================================================
def crear_venta(codigo_venta,
                cliente_venta,
                empleado_venta,
                medicamento,
                cantidad,
                precio_unitario,
                total):
    return {
        'Codigo': codigo_venta,
        'Cliente': cliente_venta,
        'Empleado': empleado_venta,
        'Medicamento': medicamento,
        'Cantidad': cantidad,
        'Precio_Unitario': precio_unitario,
        'Total': total
    }



# =======================================================================================
#                                       REGISTRAR VENTA
# =======================================================================================
def registrar_venta():
    codigo_venta = obtener_codigo_venta()

    cliente_venta = obtener_cliente()
    if cliente_venta is None:
        return 
    
    empleado_venta = obtener_empleado()
    if empleado_venta is None:
        return
    
    medicamento_venta = obtener_medicamento()
    if medicamento_venta is None:
        return
    
    cantidad_a_vender = obtener_cantidad_vender()
    if cantidad_a_vender > medicamento_venta['Stock']:
        print('\nNo hay suficiente stock.\n')
        return
    

    precio_unitario = medicamento_venta['Precio_Venta']
    total = cantidad_a_vender * precio_unitario


    venta = crear_venta(
            codigo_venta,
            cliente_venta['Nombre'],
            empleado_venta['Nombre'],
            medicamento_venta['Nombre'],
            cantidad_a_vender,
            precio_unitario,
            total
            )
    
    ventas.append(venta)

    medicamento_venta['Stock'] -= cantidad_a_vender

    print('\nVenta realizada correctamente.\n')


# =======================================================================================
#                                      MOSTRAR VENTAS
# =======================================================================================
def mostrar_ventas():
    if ventas:
        for i, venta in enumerate(ventas):
            print(f'''
            {i + 1}
            ====================================
                            VENTA
            ====================================
            Codigo            : {venta['Codigo']}
            Cliente           : {venta['Cliente']}
            Empleado          : {venta['Empleado']}
            Medicamento       : {venta['Medicamento']}
            Cantidad          : {venta['Cantidad']}
            Precio Unitario   : RD${venta['Precio_Unitario']:.2f}
            Total             : RD${venta['Total']:.2f}
            ====================================
            ''')

        print(f'\nTotal de ventas: {len(ventas)}\n')

    else:
        print('\nNo hay ventas registradas.\n')


# =======================================================================================
#                                       BUSCAR MEDICAMENTO
# =======================================================================================
def buscar_venta():
    if ventas:
        encontrado = False
        codigo_venta_buscado = input('Codigo de venta a buscar: ').strip().upper()

        if codigo_venta_buscado == "":
            print('\nCodigo de venta invalido.\n')
            return
        
        for i, venta in enumerate(ventas):
            if venta['Codigo'] == codigo_venta_buscado:
                encontrado = True
                print('\nVenta encontrada.\n')
                print(f'''
                {i + 1}
                ====================================
                                VENTA
                ====================================
                Codigo            : {venta['Codigo']}
                Cliente           : {venta['Cliente']}
                Empleado          : {venta['Empleado']}
                Medicamento       : {venta['Medicamento']}
                Cantidad          : {venta['Cantidad']}
                Precio Unitario   : RD${venta['Precio_Unitario']:.2f}
                Total             : RD${venta['Total']:.2f}
                ====================================
                ''')
                break

        if not encontrado:
            print('\nVenta no encontrada.\n')
    
    else:
        print('\nNo hay ventas registradas.\n')

# =======================================================================================
#                                     ELIMINAR VENTA  
# =======================================================================================
def eliminar_venta():
    if ventas:
        encontrado = False
        codigo_venta_buscado = input('Codigo de venta a buscar: ').strip().upper()

        if codigo_venta_buscado == "":
            print('\nCodigo de venta invalido.\n')
            return
        
        for i, venta in enumerate(ventas):
            if venta['Codigo'] == codigo_venta_buscado:
                encontrado = True
                print('\nVenta encontrada.\n')
                print(f'''
                {i + 1}
                ====================================
                                VENTA
                ====================================
                Codigo            : {venta['Codigo']}
                Cliente           : {venta['Cliente']}
                Empleado          : {venta['Empleado']}
                Medicamento       : {venta['Medicamento']}
                Cantidad          : {venta['Cantidad']}
                Precio Unitario   : RD${venta['Precio_Unitario']:.2f}
                Total             : RD${venta['Total']:.2f}
                ====================================
                ''')
                ventas.remove(venta)
                print('\nVenta eliminada correctamente.\n')
                break

        if not encontrado:
            print('\nVenta no encontrada.\n')
    
    else:
        print('\nNo hay ventas registradas.\n')

# =======================================================================================
#                                      MENU DEL SISTEMA 
# =======================================================================================
def menu_ventas():
    while True:
        mostrar_menu_ventas()

        try:
            opcion = int(input('Elija una opcion: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue
        
        limpiar_consola()

        if opcion == 1:
            registrar_venta()

        elif opcion == 2:
            mostrar_ventas()

        elif opcion == 3:
            buscar_venta()

        elif opcion == 4:
            eliminar_venta()

        elif opcion == 5:
            print('\nVolviendo al menu principal.\n')
            break
        else:
            print('\nOpcion invalida.\n')