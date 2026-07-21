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
#                                    OBTENER DATOS
# ==============================================================================================
def obtener_texto(prompt):
    while True:
            dato = input(prompt).strip().title()
            if dato == 'Salir':
                return None
            
            if dato == "":
                print('\n[ Dato invalido. ]\n')
                continue
    
            return dato
        
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
        correo_empresa = obtener_texto('Ingrese el correo de la empresa: ')

        if not ('@' in correo_empresa and '.' in correo_empresa):
            print('\nCorreo invalido.\n')
            continue
            
        return correo_empresa
    
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
    nombre_empresa = obtener_texto('Ingrese el nombre de la empresa: ')

    if nombre_empresa is None:
        return 
    
    for proveedor in proveedores:
        if proveedor['Nombre'] == nombre_empresa:
            existe = True
            break

    if existe:
        print('\n[ El proveedor ya existe. ]\n')
        return
    
    telefono_empresa = obtener_telefono_empresa()
    correo_empresa = obtener_correo_empresa()
    direccion_empresa = obtener_texto('ingrese la direccion de la empresa: ')
    ciudad_empresa = obtener_texto('Ingrese la ciudad de la empresa: ')

    proveedor = crear_proveedor(codigo,
                                nombre_empresa,
                                telefono_empresa,
                                correo_empresa,
                                direccion_empresa,
                                ciudad_empresa
                                )

    proveedores.append(proveedor)
    guardar_proveedores(proveedores)
    print('\n[ Proveedor agregado correctamente. ]\n')
    
    
# ==============================================================================================
#                                       MOSTRAR PROVEEDOR
# ==============================================================================================
def mostrar_proveedor(i, proveedor):
    print(f'''
    {i + 1}
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
            


# ==============================================================================================
#                                       MOSTRAR PROVEEDORES
# ==============================================================================================
def mostrar_proveedores():
    if proveedores:
        for i, proveedor in enumerate(proveedores):
            mostrar_proveedor(i, proveedor)

        print(f'\n[ Total de proveedores: {len(proveedores)} ]\n')

    else:
        print('\n[ No hay proveedores registrados. ]\n')

# ==============================================================================================
#                                       BUSCAR POR CODIGO
# ==============================================================================================
def buscar_codigo(codigo):
    for i, proveedor in enumerate(proveedores):
        if proveedor['Codigo'] == codigo:
            return i, proveedor
        
    return None, None

# ==============================================================================================
#                                       BUSCAR PROVEEDOR
# ==============================================================================================
def buscar_proveedor():
    codigo_proveedor_buscado = input('Ingrese el codigo de la empresa a buscar: ').strip().upper()
    i, proveedor = buscar_codigo(codigo_proveedor_buscado)
        
    if proveedor:
        mostrar_proveedor(i, proveedor)
            
    else:
        print('\n[ Proveedor no encontrado. ]\n')



# ==============================================================================================
#                                       ACTUALIZAR PROVEEDOR
# ==============================================================================================
def actualizar_proveedor():
    codigo_proveedor_buscado = input('Ingrese el codigo de la empresa a buscar: ').strip().upper()
    i, proveedor = buscar_codigo(codigo_proveedor_buscado)
    if proveedor:
        mostrar_proveedor(i, proveedor)

        # ----------------------------------
        #         VERIFICAR TELEFONO
        # ----------------------------------
        nuevo_telefono = obtener_telefono_empresa()

        proveedor_existe = False
        for otro_proveedor in proveedores:
            if (otro_proveedor['Codigo'] != proveedor['Codigo'] 
                and otro_proveedor['Telefono'] == nuevo_telefono):
                proveedor_existe = True
                break
            if proveedor_existe:
                print('\n[ El proveedor ya existe. ]\n')
                return
            
            proveedor['Telefono'] = nuevo_telefono


            # ----------------------------------
            #         VERIFICAR CORREO
            # ----------------------------------
            nuevo_correo = obtener_correo_empresa()
            correo_existe = False
            for otro_proveedor in proveedores:
                if (otro_proveedor['Codigo'] != proveedor['Codigo'] 
                    and otro_proveedor['Correo'] == nuevo_correo):
                    correo_existe = True
                    break
            if correo_existe:
                print('\n[ El correo ya existe. ]\n')
                return
            
            proveedor['Correo'] = nuevo_correo
            proveedor['Direccion'] = obtener_texto('Ingrese la direccion de la empresa: ')
            proveedor['Ciudad'] = obtener_texto('Ingrese la ciudad de la empresa: ')
            guardar_proveedores(proveedores)
            print('\n[ Proveedor actualizado correctamente. ]\n')
            break
    else:
        print('\n[ No hay proveedores registrados. ]\n')


# ==============================================================================================
#                                       ELIMINAR PROVEEDOR
# ==============================================================================================
def eliminar_proveedor():
    codigo_proveedor_buscado = input('Ingrese el codigo de la empresa a buscar: ').strip().upper()
    i, proveedor = buscar_codigo(codigo_proveedor_buscado)
    if proveedor:
        mostrar_proveedor(i, proveedor)
        
        eliminar = input('Desea eliminar este proveedor: ').strip().lower()
        if eliminar == 'si':
            proveedores.remove(proveedor)
            guardar_proveedores(proveedores)
            print('\n[ Proveedor eliminado correctamente. ]\n')
            
        else:
            print('\n[ El proveedor no ha sido eliminado. ]\n')

    
    else:
        print('\n[ No hay proveedores registrados. ]\n')


# ==============================================================================================
#                                       SISTEMA PRINCIPAL
# ==============================================================================================
def menu_proveedores():
    while True:
        mostrar_menu()

        try:
            opcion = int(input('Elije una opcion: '))

        except ValueError:
            print('\n[ Dato invalido. ]\n')
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
            print('\n[ Volviendo al menu principal. ]\n')
            break
        else:
            print('\n [ Opcion invalida. ]\n')