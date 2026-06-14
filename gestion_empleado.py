# ================================================================================================
#                                       GESTION EMPLEADOS
# ================================================================================================
from utilidades import limpiar_consola
from persistencia import guardar_empleados
from persistencia import cargar_empleados
# ================================================================================================
#                                           DATOS
# ================================================================================================
empleados = cargar_empleados()
contador_empleados = len(empleados) + 1

# ================================================================================================
#                                       MENU EMPLEADOS
# ================================================================================================
def mostrar_menu():
    print('''
    ====================================
                EMPLEADOS
    ====================================

    1. Registrar empleado
    2. Mostrar empleados
    3. Buscar empleado
    4. Actualizar empleado
    5. Eliminar empleado
    6. Volver

    ====================================
    ''')


# ================================================================================================
#                                       CARGO EMPLEADO
# ================================================================================================
def mostrar_cargo_empleado():
    print('''
    ====================================
            CARGOS EMPLEADOS
    ====================================
    1. Farmacéutico
    2. Cajero
    3. Supervisor
    4. Administrador
    ====================================
    ''')

# ================================================================================================
#                                      OBTENER CODIGO DEL EMPLEADO
# ================================================================================================
def obtener_codigo_empleado():
    global contador_empleados

    codigo_empleado = f'EMP-{contador_empleados:03}'
    contador_empleados += 1

    return codigo_empleado

# ================================================================================================
#                               OBTENER NOMBRE DEL EMPLEADO        
# ================================================================================================
def obtener_nombre_empleado():
    while True:
        nombre_empleado = input('Nombre empleado: ').strip().title()

        if nombre_empleado == 'Salir':
            return None
        
        if nombre_empleado == "":
            print('\nNombre del empleado invalido.\n')
            continue

        return nombre_empleado
    
# ================================================================================================
#                                       OBTENER CARGO DEL EMPLEADO
# ================================================================================================
def obtener_cargo_empleado():
    while True:
        mostrar_cargo_empleado()

        try:
            cargo_empleado = int(input('Elija el cargo del empleado: '))
        
        except ValueError:
            print('\nDato invalido.\n')
            continue

        if cargo_empleado == 1:
            return 'Farmacéutico'
        
        elif cargo_empleado == 2:
            return 'Cajero'
        
        elif cargo_empleado == 3:
            return 'Supervisor'
        
        elif cargo_empleado == 4:
            return 'Administrador'
        
        else:
            print('\nCargo invalido.\n')


# ================================================================================================
#                                OBTENER TELEFONO DEL EMPLEADO
# ================================================================================================
def obtener_telefono_empleado():
    while True:
        
        telefono_empleado = input('Telefono del empleado: ').strip()

        if not telefono_empleado.isdigit():
            print('\nTelefono invalido.\n')
            continue

        if len(str(telefono_empleado)) != 10:
            print('\nNumero de telefono invalido.\n')
            continue
        
        if str(telefono_empleado)[:3] not in ['809', '829', '849']:
            print('\nNumero de telefono invalido.\n')
            continue
        
        telefono_empleado = f'({telefono_empleado[:3]}) {telefono_empleado[3:6]} {telefono_empleado[6:]}'
        return telefono_empleado
    

# ================================================================================================
#                                OBTENER CORREO DEL EMPLEADO     
# ================================================================================================
def obtener_correo_empleado():
    while True:
        correo_empleado = input('Correo del empleado: ').strip().lower()

        if correo_empleado == "":
            print('\nCorreo empleado incorrecto.\n')
            continue

        if not ('@' in correo_empleado and '.' in correo_empleado):
            print('\nCorreo invalido.\n')
            continue
            
        return correo_empleado
    

# ================================================================================================
#                                   OBTENER SALARIO DEL EMPLEADO
# ================================================================================================
def obtener_salario_empleado():
    while True:
        try:
            salario_empleado = float(input('Salario del empleado: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue

        if salario_empleado <= 0:
            print('\nSalario del empleado incorrecto.\n')
            continue

        return salario_empleado
    


# -----------------------------------------------------------------------------------------------

# ================================================================================================
#                                         CREAR EL EMPLEADO
# ================================================================================================
def crear_empleado(codigo_empleado, nombre_empleado, cargo_empleado, telefono_empleado, correo_empleado, salario_empleado):
    return {
        'Codigo': codigo_empleado,
        'Nombre': nombre_empleado,
        'Cargo': cargo_empleado,
        'Telefono': telefono_empleado,
        'Correo': correo_empleado,
        'Salario': salario_empleado
    }

# ================================================================================================
#                                      REGISTRAR EMPLEADO
# ================================================================================================
def registrar_empleado():
    existe = False
    codigo_empleado = obtener_codigo_empleado()
    nombre_empleado = obtener_nombre_empleado()

    if nombre_empleado is None:
        return
    
    for empleado in empleados:
        if empleado['Nombre'] == nombre_empleado:
            existe = True
            break

    if existe:
        print('\nEl empleado ya existe.\n')
        return
    
    cargo_empleado = obtener_cargo_empleado()

    telefono_empleado = obtener_telefono_empleado()
    for empleado in empleados:
        if empleado['Telefono'] == telefono_empleado:
            print('\nEl telefono ya existe.\n')
            return
    
    correo_empleado = obtener_correo_empleado()
    for empleado in empleados:
        if empleado['Correo'] == correo_empleado:
            print('\nEl Correo ya existe.\n')
            return
        
    salario_empleado = obtener_salario_empleado()

    empleado = crear_empleado(codigo_empleado,
                              nombre_empleado,
                              cargo_empleado,
                              telefono_empleado,
                              correo_empleado,
                              salario_empleado)
    
    empleados.append(empleado)
    guardar_empleados(empleados)

    print('\nEmpleado agregado correctamente.\n')


# ================================================================================================
#                                       MOSTRAR LOS EMPLEADOS       
# ================================================================================================
def mostrar_empleados():
    if empleados:
        for i, empleado in enumerate(empleados):
            print(f'''
            =============================================
            {i + 1}   EMPLEADO
            =============================================
            Codigo     : {empleado['Codigo']}
            Nombre     : {empleado['Nombre']}
            Cargo      : {empleado['Cargo']}
            Telefono   : {empleado['Telefono']}
            Correo     : {empleado['Correo']}
            Salario    : RD${empleado['Salario']:.2f}
            =============================================
            ''')
        print(f'\nTotal de empleados: {len(empleados)}\n')

    else:
        print('\nNo hay empleados registrados.\n')


# ================================================================================================
#                                       BUSCAR EMPLEADO       
# ================================================================================================
def buscar_empleado():
    if empleados:
        encontrado = False
        codigo_empleado_buscado = input('Codigo del empleado: ').strip().upper()
        if codigo_empleado_buscado == "":
            print('\nCodigo invalido.\n')
            return
               
        for i, empleado in enumerate(empleados):

            if empleado['Codigo'] == codigo_empleado_buscado:
                
                encontrado = True
                print('\nEmpleado encontrado.\n')
                print(f'''
                =============================================
                {i + 1}   EMPLEADO
                =============================================
                Codigo     : {empleado['Codigo']}
                Nombre     : {empleado['Nombre']}
                Cargo      : {empleado['Cargo']}
                Telefono   : {empleado['Telefono']}
                Correo     : {empleado['Correo']}
                Salario    : RD${empleado['Salario']:.2f}
                =============================================
                ''')
                break

        if not encontrado:
            print('\nEmpleado no encontrado.\n')

    else:
        print('\nNo hay empleados registrados.\n')


# ================================================================================================
#                                       ACTUALIZAR EMPLEADO         
# ================================================================================================
def actualizar_empleado():
    if empleados:
        encontrado = False
        codigo_empleado_buscado = input('Codigo del empleado: ').strip().upper()
        if codigo_empleado_buscado == "":
            print('\nCodigo invalido.\n')
            return
        
        for i, empleado in enumerate(empleados):

            if empleado['Codigo'] == codigo_empleado_buscado:
                
                encontrado = True
                print('\nEmpleado encontrado.\n')
                print(f'''
                =============================================
                {i + 1}   EMPLEADO
                =============================================
                Codigo     : {empleado['Codigo']}
                Nombre     : {empleado['Nombre']}
                Cargo      : {empleado['Cargo']}
                Telefono   : {empleado['Telefono']}
                Correo     : {empleado['Correo']}
                Salario    : RD${empleado['Salario']:.2f}
                =============================================
                ''')
                empleado['Cargo'] = obtener_cargo_empleado()

                # ----------------------------------
                #         VERIFICAR TELEFONO
                # ----------------------------------
                nuevo_telefono = obtener_telefono_empleado()

                telefono_existe = False
                for otro_empleado in empleados:
                    if (otro_empleado['Codigo'] != empleado['Codigo'] 
                        and otro_empleado['Telefono'] == empleado['Telefono']):
                        telefono_existe = True
                        break
                if telefono_existe:
                    print('\nEl telefono ya existe.\n')
                    return
                
                empleado['Telefono'] = nuevo_telefono
                # ----------------------------------
                #         VERIFICAR CORREO
                # ----------------------------------
                nuevo_correo = obtener_correo_empleado()
                correo_existe = False
                for otro_empleado in empleados:
                    if (otro_empleado['Codigo'] != empleado['Codigo'] 
                        and otro_empleado['Correo'] == empleado['Correo']):
                        correo_existe = True
                        break

                if correo_existe:
                    print('\nEl correo ya existe.\n')
                    return
                
                empleado['Correo'] = obtener_correo_empleado()
                empleado['Salario'] = obtener_salario_empleado()

                guardar_empleados(empleados)
                print('\nEmpleado actualizado correctamente.\n')
                break

        if not encontrado:
            print('\nEmpleado no encontrado.\n')
        
    else:
        print('\nNo hay empleados registrados.\n')


# ================================================================================================
#                                       ELIMINAR EMPLEADO
# ================================================================================================
def eliminar_empleado():
    if empleados:
        encontrado = False
        codigo_empleado_buscado = input('Codigo del empleado: ').strip().upper()

        if codigo_empleado_buscado == "":
            print('\nCodigo invalido.\n')
            return
        for i, empleado in enumerate(empleados):

            if empleado['Codigo'] == codigo_empleado_buscado:

                
                encontrado = True
                print('\nEmpleado encontrado.\n')
                print(f'''
                =============================================
                {i + 1}   EMPLEADO
                =============================================
                Codigo     : {empleado['Codigo']}
                Nombre     : {empleado['Nombre']}
                Cargo      : {empleado['Cargo']}
                Telefono   : {empleado['Telefono']}
                Correo     : {empleado['Correo']}
                Salario    : RD${empleado['Salario']:.2f}
                =============================================
                ''')
                empleados.remove(empleado)
                
                guardar_empleados(empleados)
                print('\nEmpleado eliminado correctamente.\n')
                break

        if not encontrado:
            print('\nEmpleado no encontrado.\n')

    else:
        print('\nNo hay empleados registrados.\n')


# ==============================================================================================
#                                       SISTEMA PRINCIPAL
# ==============================================================================================
def menu_empleados():
    while True:
        mostrar_menu()

        try:
            opcion = int(input('Elije una opcion: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue
        
        limpiar_consola()

        if opcion == 1:
            registrar_empleado()

        elif opcion == 2:
            mostrar_empleados()

        elif opcion == 3:
            buscar_empleado()

        elif opcion == 4:
            actualizar_empleado()

        elif opcion == 5:
            eliminar_empleado()

        elif opcion == 6:
            print('\nVolviendo al menu principal.\n')
            break
        else:
            print('\nOpcion invalida.\n')