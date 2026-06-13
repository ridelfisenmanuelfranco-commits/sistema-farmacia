# ===============================================================================================
#                                       GESTION DE PROVEEDORES
# ===============================================================================================

from utilidades import limpiar_consola
from persistencia import guardar_proveedores
from persistencia import cargar_proveedores

# ===============================================================================================
#                                          DATOS
# ===============================================================================================
proveedores = cargar_proveedores()
contador_proveedores = len(proveedores) + 1

# ===============================================================================================
#                                       MENU DE PROVEEDORES
# ===============================================================================================
def mostrar_menu():
    print('''
    ====================================
            PROVEEDORES
    ====================================

    1. Registrar proveedor
    2. Mostrar proveedores
    3. Buscar proveedor
    4. Actualizar proveedor
    5. Eliminar proveedor
    6. Volver

    ====================================
    ''')

# ===============================================================================================
#                                    OBTENER CODIGO DEL PROVEEDOR
# ===============================================================================================
def obtener_codigo_proveedor():
    global contador_proveedores

    codigo_proveedor = f'PRO-{contador_proveedores:03}'
    contador_proveedores += 1

    return codigo_proveedor


# ==============================================================================================
#                                    OBTENER NOMBRE DE LA EMPRESA
# ==============================================================================================
def obtener_nombre_empresa():
    while True:
        nombre_empresa = input('Nombre de la empresa: ').strip().title()
        if nombre_empresa == 'Salir':
            return None
        
        if nombre_empresa == "":
            print('\nNombre de la empresa invalido.\n')
            continue

        return nombre_empresa
    
# ==============================================================================================
#                                    OBTENER TELEFONO DE LA EMPRESA
# ==============================================================================================
def obtener_telefono_empresa():
    while True:
        
        telefono_empresa = input('Telefono de la empresa: ').strip()

        if not telefono_empresa.isdigit():
            print('\nTelefono invalido.\n')
            continue

        if len(str(telefono_empresa)) != 10:
            print('\nNumero de telefono invalido.\n')
            continue
        
        if str(telefono_empresa)[:3] not in ['809', '829', '849']:
            print('\nNumero de telefono invalido.\n')
            continue
        
        telefono_empresa = f'({telefono_empresa[:3]}) {telefono_empresa[3:6]} {telefono_empresa[6:]}'
        return telefono_empresa
    

# ==============================================================================================
#                                      OBTENER CORREO DE LA EMPRESA
# ==============================================================================================
def obtener_correo_empresa():
    while True:
        correo_empresa = input('Correo de la empresa: ').strip().lower()

        if correo_empresa == "":
            print('\nCorreo invalido.\n')
            continue

        if not ('@' in correo_empresa and '.' in correo_empresa):
            print('\nCorreo invalido.\n')
            continue
            
        return correo_empresa
    
# ==============================================================================================
#                                  OBTENER DIRECCION DE LA EMPRESA
# ==============================================================================================
def obtener_direccion_empresa():
    while True:
        direccion_empresa = input('Direccion de la empresa: ').strip().title()

        if direccion_empresa == "":
            print('\nDireccion de empresa invalida.\n')
            continue

        return direccion_empresa
    

# ==============================================================================================
#                                      OBTENER CIUDAD DE LA EMPRESA
# ==============================================================================================
def obtener_ciudad_empresa():
    while True:
        ciudad_empresa = input('Ciudad de la empresa: ').strip().title()

        if ciudad_empresa == "":
            print('\nNombre de la ciudad invalido.\n')
            continue

        return ciudad_empresa
    

# ==============================================================================================
#                                        CREAR PROVEEDOR
# ==============================================================================================
def crear_proveedor(codigo, nombre, telefono, correo, direccion, ciudad):
    return {
        'Codigo': codigo,
        'Nombre': nombre,
        'Telefono': telefono,
        'Correo': correo,
        'Direccion': direccion,
        'Ciudad': ciudad
    }

# ==============================================================================================
#                                       REGISTRAR PROVEEDOR
# ==============================================================================================
def registrar_proveedor():
    existe = False
    codigo = obtener_codigo_proveedor()
    nombre_empresa = obtener_nombre_empresa()

    if nombre_empresa is None:
        return 
    
    for proveedor in proveedores:
        if proveedor['Nombre'] == nombre_empresa:
            existe = True
            break

    if existe:
        print('\nEl proveedor ya existe.\n')
        return
    
    telefono_empresa = obtener_telefono_empresa()
    correo_empresa = obtener_correo_empresa()
    direccion_empresa = obtener_direccion_empresa()
    ciudad_empresa = obtener_ciudad_empresa()

    proveedor = crear_proveedor(codigo,
                                nombre_empresa,
                                telefono_empresa,
                                correo_empresa,
                                direccion_empresa,
                                ciudad_empresa
                                )

    proveedores.append(proveedor)
    guardar_proveedores(proveedores)
    print('\nProveedor agregado correctamente.\n')

# ==============================================================================================
#                                       MOSTRAR PROVEEDOR
# ==============================================================================================
def mostrar_proveedores():
    if proveedores:
        for  proveedor in proveedores:
            print(f'''
            ========================================
                        PROVEEDOR
            ========================================
            Codigo     : {proveedor['Codigo']}
            Nombre     : {proveedor['Nombre']}
            Telefono   : {proveedor['Telefono']}
            Correo     : {proveedor['Correo']}
            Direccion  : {proveedor['Direccion']}
            Ciudad     : {proveedor['Ciudad']}
            ========================================
            ''')

        print(f'\nTotal de proveedores: {len(proveedores)}\n')

    else:
        print('\nNo hay proveedores registrados.\n')


# ==============================================================================================
#                                       BUSCAR PROVEEDOR
# ==============================================================================================
def buscar_proveedor():
    if proveedores:
        encontrado = False
        nombre_proveedor_buscado = obtener_nombre_empresa()

        for proveedor in proveedores:
            if proveedor['Nombre'] == nombre_proveedor_buscado:
                encontrado = True
                print('\nProveedor encontrado.\n')
                print(f'''
                ========================================
                            PROVEEDOR
                ========================================
                Codigo     : {proveedor['Codigo']}
                Nombre     : {proveedor['Nombre']}
                Telefono   : {proveedor['Telefono']}
                Correo     : {proveedor['Correo']}
                Direccion  : {proveedor['Direccion']}
                Ciudad     : {proveedor['Ciudad']}
                ========================================
                ''')
                break

        if not encontrado:
            print('\nProveedor no encontrado.\n')

    else:
        print('\nNo hay proveedores registrados.\n')



# ==============================================================================================
#                                       ACTUALIZAR PROVEEDOR
# ==============================================================================================
def actualizar_proveedor():
    if proveedores:
        encontrado = False
        nombre_proveedor_buscado = obtener_nombre_empresa()

        for proveedor in proveedores:
            if proveedor['Nombre'] == nombre_proveedor_buscado:
                encontrado = True
                print('\nProveedor encontrado.\n')
                print(f'''
                ========================================
                            PROVEEDOR
                ========================================
                Codigo     : {proveedor['Codigo']}
                Nombre     : {proveedor['Nombre']}
                Telefono   : {proveedor['Telefono']}
                Correo     : {proveedor['Correo']}
                Direccion  : {proveedor['Direccion']}
                Ciudad     : {proveedor['Ciudad']}
                ========================================
                ''')

                proveedor['Telefono'] = obtener_telefono_empresa()
                proveedor['Correo'] = obtener_correo_empresa()
                proveedor['Direccion'] = obtener_direccion_empresa()
                proveedor['Ciudad'] = obtener_ciudad_empresa()

                guardar_proveedores(proveedores)
                print('\nProveedor actualizado correctamente.\n')
                break
        if not encontrado:
            print('\nProveedor no encontrado.\n')

    else:
        print('\nNo hay proveedores registrados.\n')


# ==============================================================================================
#                                       ELIMINAR PROVEEDOR
# ==============================================================================================
def eliminar_proveedor():
    if proveedores:
        encontrado = False
        nombre_proveedor_buscado = obtener_nombre_empresa()

        for proveedor in proveedores:
            if proveedor['Nombre'] == nombre_proveedor_buscado:
                encontrado = True
                print('\nProveedor encontrado.\n')
                print(f'''
                ========================================
                            PROVEEDOR
                ========================================
                Codigo     : {proveedor['Codigo']}
                Nombre     : {proveedor['Nombre']}
                Telefono   : {proveedor['Telefono']}
                Correo     : {proveedor['Correo']}
                Direccion  : {proveedor['Direccion']}
                Ciudad     : {proveedor['Ciudad']}
                ========================================
                ''')

                proveedores.remove(proveedor)
                guardar_proveedores(proveedores)
                print('\nProveedor eliminado correctamente.\n')
                break
                
        if not encontrado:
            print('\nProveedor no encontrado.\n')
    
    else:
        print('\nNo hay proveedores registrados.\n')


# ==============================================================================================
#                                       SISTEMA PRINCIPAL
# ==============================================================================================
def menu_proveedores():
    while True:
        mostrar_menu()

        try:
            opcion = int(input('Elije una opcion: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue
        
        limpiar_consola()

        if opcion == 1:
            registrar_proveedor()

        elif opcion == 2:
            mostrar_proveedores()

        elif opcion == 3:
            buscar_proveedor()

        elif opcion == 4:
            actualizar_proveedor()

        elif opcion == 5:
            eliminar_proveedor()

        elif opcion == 6:
            print('\nVolviendo al menu principal.\n')
            break
        else:
            print('\nOpcion invalida.\n')