# ============================================================================================
#                               SISTEMA DE GESTION DE FARMACIA
# ============================================================================================
print
# ============================================================================================
#                               FUNCIONES A IMPORTAR
# ============================================================================================
from gestion_medicamentos import menu_medicamentos
from gestion_proveedores import menu_proveedores
from gestion_empleado import menu_empleados
from gestion_cliente import menu_clientes
# ============================================================================================
#                               MENU PRINCIPAL DEL SISTEMA
# ============================================================================================
def mostrar_menu_principal():
    print('''
    ====================================
        SISTEMA DE FARMACIA
    ====================================

    1. Medicamentos
    2. Proveedores
    3. Empleados
    4. Clientes
    5. Ventas
    6. Reportes
    7. Salir

    ====================================
    ''')


# ============================================================================================
#                               SISTEMA PRINCIPAL
# ============================================================================================
while True:

    mostrar_menu_principal()

    try:
        opcion = int(input('Elija una opcion: '))

    except ValueError:
        print('\nDato invalido.\n')
        continue

    if opcion == 1:
        menu_medicamentos()
    
    elif opcion == 2:
        menu_proveedores()

    elif opcion == 3:
        menu_empleados()

    elif opcion == 4:
        menu_clientes()
        
    elif opcion == 7:
        print('\nSaliendo del sistema.\n')
        break

    else:
        print('\nOpcion invalida.\n')