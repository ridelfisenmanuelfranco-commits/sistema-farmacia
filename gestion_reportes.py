# =======================================================================================
#                               GESTION DE REPORTES               
# =======================================================================================

# =======================================================================================
#                               FUNCIONES IMPORTADAS                                       
# =======================================================================================
from utilidades import limpiar_consola

from gestion_medicamentos import medicamentos
from gestion_proveedores import proveedores
from gestion_empleado import empleados
from gestion_cliente import clientes
from gestion_ventas import ventas

# =======================================================================================
#                                 MOSTRAR MENU DE REPORTES       
# =======================================================================================
def mostrar_menu():
    print('''
    ====================================
                REPORTES
    ====================================
    1. Total de medicamentos
    2. Total de proveedores
    3. Total de empleados
    4. Total de clientes
    5. Total de ventas
    6. Medicamentos con stock bajo
    7. Ventas realizadas
    8. Volver
    ====================================
    ''')

# =======================================================================================
#                                 TOTAL MEDICAMENTOS                   
# =======================================================================================
def reporte_total_medicamentos():
    print('''
    ====================================
        REPORTE TOTAL DE MEDICAMENTOS
    ====================================
    ''')
    print(f'\nTotal de medicamentos: {len(medicamentos)}\n')


# =======================================================================================
#                                 TOTAL DE PROVEEDORES
# =======================================================================================
def reporte_total_proveedores():
    print('''
    ====================================
        REPORTE TOTAL DE PROVEEDORES
    ====================================
    ''')
    print(f'\nTotal de proveedores: {len(proveedores)}\n')


# =======================================================================================
#                                     TOTAL DE EMPLEADOS  
# =======================================================================================
def reporte_total_empleados():
    print('''
    ====================================
        REPORTE TOTAL DE EMPLEADOS
    ====================================
    ''')
    print(f'\nTotal de empleados: {len(empleados)}\n')


# =======================================================================================
#                                     TOTAL DE CLIENTES  
# =======================================================================================
def reporte_total_clientes():
    print('''
    ====================================
         REPORTE TOTAL DE CLIENTES
    ====================================
    ''')
    print(f'\nTotal de clientes: {len(clientes)}\n')


# =======================================================================================
#                                     TOTAL DE VENTAS
# =======================================================================================
def reporte_total_ventas():
    print('''
    ====================================
           REPORTE TOTAL DE VENTAS
    ====================================
    ''')
    print(f'\nTotal de ventas: {len(ventas)}\n')


# =======================================================================================
#                                       STOCK BAJO
# =======================================================================================
def reporte_stock_bajo():
    encontrado = False
    print('''
    ====================================
        MEDICAMENTOS STOCK BAJO
    ====================================
    ''')
    for medicamento in medicamentos:

        if medicamento['Stock'] <= medicamento['Stock_Minimo']:

            encontrado = True

            print(f'''
            ====================================
            Codigo : {medicamento['Codigo']}
            Nombre : {medicamento['Nombre']}
            Stock  : {medicamento['Stock']}
            Minimo : {medicamento['Stock_Minimo']}
            ====================================
            ''')

    if not encontrado:
        print('\nNo hay medicamentos con stock bajo.\n')

# =======================================================================================
#                                     REPORTES DE VENTAS 
# =======================================================================================
def reporte_ventas():
    if ventas:
        print('''
        ====================================
                 REPORTE DE VENTAS
        ====================================
        ''')
        for venta in ventas:

            print(f'''
            ====================================
            Codigo           : {venta['Codigo']}
            Cliente          : {venta['Cliente']}
            Empleado         : {venta['Empleado']}
            Medicamento      : {venta['Medicamento']}
            Cantidad         : {venta['Cantidad']}
            Precio Unitario  : RD${venta['Precio_Unitario']:.2f}
            Total            : RD${venta['Total']:.2f}
            =====================================
            ''')

    else:
        print('\nNo hay ventas registradas.\n')

# =======================================================================================
#                               MENU DE REPORTES        
# =======================================================================================
def menu_reportes():

    while True:
        mostrar_menu()

        try:
            opcion = int(input('Elija una opcion: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue

        limpiar_consola()

        if opcion == 1:
            reporte_total_medicamentos()

        elif opcion == 2:
            reporte_total_proveedores()

        elif opcion == 3:
            reporte_total_empleados()

        elif opcion == 4:
            reporte_total_clientes()

        elif opcion == 5:
            reporte_total_ventas()

        elif opcion == 6:
            reporte_stock_bajo()

        elif opcion == 7:
            reporte_ventas()

        elif opcion == 8:
            break

        else:
            print('\nOpcion invalida.\n')