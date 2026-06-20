# =======================================================================================
#                                GESTION DE MEDICAMENTO
# =======================================================================================
from utilidades import limpiar_consola
from gestion_proveedores import proveedores
from persistencia import guardar_medicamentos
from persistencia import cargar_medicamentos
# =======================================================================================
#                                       DATOS
# =======================================================================================
medicamentos = cargar_medicamentos()
contador_medicamentos = len(medicamentos) + 1

# =======================================================================================
#                                MENU DEL SISTEMA
# =======================================================================================
def mostrar_menu():
    print("""
    ====================================
        MEDICAMENTOS
    ====================================

    1. Registrar medicamento
    2. Mostrar medicamentos
    3. Buscar medicamento
    4. Actualizar medicamento
    5. Eliminar medicamento
    6. Volver

    ====================================
    """)



# =======================================================================================
#                                   OPCIONES CATEGORIA               
# =======================================================================================
def mostrar_categorias():
    print("""
    ====================================
                CATEGORIAS
    ====================================

    1. Analgésicos
    2. Antibióticos
    3. Antiinflamatorios
    4. Antialérgicos
    5. Vitaminas
    6. Jarabes
    7. Otros

    ====================================
    """)


# =======================================================================================
#                                    OPCIONES PROVEEDOR  
# =======================================================================================
def mostrar_proveedores():
    if proveedores:

        for i, proveedor in enumerate(proveedores):
            print(f'{i + 1}. {proveedor["Nombre"]}')

    else:
        print('\nNo hay proveedores registrados.\n')


# =======================================================================================
#                               OBTENER CODIGO DEL MEDICAMENTO   
# =======================================================================================
def obtener_codigo_medicamento():
    global contador_medicamentos

    codigo_medicamento = f'MED-{contador_medicamentos:03}'
    contador_medicamentos += 1

    return codigo_medicamento


# =======================================================================================
#                               OBTENER NOMBRE DEL MEDICAMENTO
# =======================================================================================
def obtener_nombre_medicamento():
    while True:
        nombre_medicamento = input('Nombre del medicamento: ').strip().title()
        if nombre_medicamento == "Salir":
            return None
        
        if nombre_medicamento == "":
            print('\nNombre del medicamento incorrecto.\n')
            continue

        return nombre_medicamento
    

# =======================================================================================
#                            OBTENER CATEGORIA DEL MEDICAMENTO
# =======================================================================================
def obtener_categoria_medicamento():
    while True:
        mostrar_categorias()

        try:
            categoria = int(input('Elija una categoria: '))
        
        except ValueError:
            print('\nDato invalido.\n')
            continue

        if categoria == 1:
            return "Analgésicos"

        elif categoria == 2:
            return "Antibióticos"

        elif categoria == 3:
            return "Antiinflamatorios"
        
        elif categoria == 4:
            return "Antialérgicos"
        
        elif categoria == 5:
            return "Vitaminas"
        
        elif categoria == 6:
            return "Jarabes"
        
        elif categoria == 7:
            return "Otros"
        
        else:
            print('\nCategoria invalida.\n')
        

# =======================================================================================
#                          OBTENER PRECIO COMPRA DEL MEDICAMENTO
# =======================================================================================
def obtener_precio_compra_medicamento():
    while True:
        try:
            precio_compra_medicamento = float(input('Precio compra del medicamento: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue

        if precio_compra_medicamento <= 0:
            print('\nPrecio del medicamento incorrecto.\n')
            continue

        return precio_compra_medicamento
    

# =======================================================================================
#                         OBTENER PRECIO DE VENTA DEL MEDICAMENTO
# =======================================================================================
def obtener_precio_venta_medicamento():
    while True:
        try:
            precio_venta_medicamento = float(input('Precio de venta del medicamento: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue

        if precio_venta_medicamento <= 0:
            print('\nPrecio de venta invalido.\n')
            continue

        return precio_venta_medicamento
    

# =======================================================================================
#                           OBTENER STOCK DEL MEDICAMENTO
# =======================================================================================
def obtener_stock_medicamento():
    while True:
        try:
            stock_medicamento = int(input('Stock del medicamento: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue

        if stock_medicamento <= 0:
            print('\nStock del medicamento incorrecto.\n')
            continue

        return stock_medicamento
    

# =======================================================================================
#                         OBTENER STOCK MINIMO DEL MEDICAMENTO
# =======================================================================================
def obtener_stock_minimo_medicamento():
    while True:
        try:
            stock_minimo_medicamento = int(input('Stock minimo del medicamento: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue


        if  stock_minimo_medicamento <= 0:
            print('\nStock minimo incorrecto.\n')
            continue

        return stock_minimo_medicamento
    

# =======================================================================================
#                       OBTENER PROVEEDOR DEL MEDICAMENTO 
# =======================================================================================
def obtener_proveedor_medicamento():
    if not proveedores:
        print('\nNo hay proveedores registrados.\n')
        return None
    
    while True:

        mostrar_proveedores()

        try:
            opcion = int(input('Elija el proveedor: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue

        if 1 <= opcion <= len(proveedores):
            return proveedores[opcion - 1]['Nombre']

        print('\nProveedor invalido.\n')



#------------------------------------------------------------------------------------------------
# =======================================================================================
#                                   CREAR MEDICAMENTO               
# =======================================================================================
def crear_medicamento(codigo, 
                      nombre,
                      categoria,
                      precio_compra,
                      precio_venta,
                      stock,
                      stock_minimo,
                      proveedor):
    return {
        "Codigo": codigo,
        "Nombre": nombre,
        "Categoria": categoria,
        "Precio_Compra": precio_compra,
        "Precio_Venta": precio_venta,
        "Stock": stock,
        "Stock_Minimo": stock_minimo,
        "Proveedor": proveedor
    }
    

# ----------------------------------------------------------------------------------------------
# =======================================================================================
#                                   REGISTRAR MEDICAMENTO                   
# =======================================================================================
def registrar_medicamento():
    existe = False

    codigo_medicamento = obtener_codigo_medicamento()
    
    nombre_medicamento = obtener_nombre_medicamento()

    if nombre_medicamento is None:
        return
    
    for medicamento in medicamentos:
        if medicamento['Nombre'] == nombre_medicamento:
            existe = True
            break
    
    if existe:
        print('\nEl medicamento ya existe.\n')
        return
    
    categoria_medicamento = obtener_categoria_medicamento()
    precio_compra = obtener_precio_compra_medicamento()
    precio_venta = obtener_precio_venta_medicamento()

    if precio_venta <= precio_compra:
        print('\nPrecio de venta invalido.\n')
        return
    
    stock_medicamento = obtener_stock_medicamento()
    stock_minimo_medicamento = obtener_stock_minimo_medicamento()
    if stock_minimo_medicamento > stock_medicamento:
        print('\nStock minimo invalido.\n')
        return
    
    proveedor_medicamento = obtener_proveedor_medicamento()
    if proveedor_medicamento is None:
        return
    
    medicamento = crear_medicamento(
        codigo_medicamento,
        nombre_medicamento,
        categoria_medicamento,
        precio_compra,
        precio_venta,
        stock_medicamento,
        stock_minimo_medicamento,
        proveedor_medicamento
        )
    
    medicamentos.append(medicamento)
    guardar_medicamentos(medicamentos)
    print('\nMedicamento agregado correctamente.\n')
    
# =======================================================================================
#                                   MOSTRAR MEDICAMENTO
# =======================================================================================    
def mostrar_medicamento(medicamento):
    print(f'''
            ========================================
                        MEDICAMENTO
            ========================================
            Codigo          : {medicamento['Codigo']}
            Nombre          : {medicamento['Nombre']}
            Categoria       : {medicamento['Categoria']}
            Precio Compra   : RD${medicamento['Precio_Compra']:.2f}
            Precio Venta    : RD${medicamento['Precio_Venta']:.2f}
            Stock           : {medicamento['Stock']}
            Stock Minimo    : {medicamento['Stock_Minimo']}
            Proveedor       : {medicamento['Proveedor']}
            ========================================
            ''')
    
    
# =======================================================================================
#                                   MOSTRAR MEDICAMENTOS
# =======================================================================================
def mostrar_medicamentos():
    if medicamentos:
        for medicamento in medicamentos:
            mostrar_medicamento(medicamento)

        print(f'\nTotal de medicamentos: {len(medicamentos)}\n')

    else:
        print('\nNo hay medicamentos registrados.\n')


# =======================================================================================
#                                BUSCAR MEDICAMENTO                          
# =======================================================================================
def buscar_medicamento():
    if medicamentos:
        encontrado = False

        nombre_medicamento_buscado = obtener_nombre_medicamento()

        for medicamento in medicamentos:
            if medicamento['Nombre'] == nombre_medicamento_buscado:
                encontrado = True
                print('\nMedicamento encontrado.\n')

                mostrar_medicamento(medicamento)
                break

        if not encontrado:
            print('\nMedicamento no encontrado.\n')

    else:
        print('\nNo hay medicamentos registrados.\n')


# =======================================================================================
#                                   ACTUALIZAR MEDICAMENTOS
# =======================================================================================
def actualizar_medicamento():
    if medicamentos:
        encontrado = False
        nombre_medicamento_buscado = obtener_nombre_medicamento()

        for medicamento in medicamentos:
            if medicamento['Nombre'] == nombre_medicamento_buscado:
                encontrado = True
                print('\nMedicamento encontrado.\n')
                mostrar_medicamento(medicamento)

                medicamento['Categoria'] = obtener_categoria_medicamento()
                medicamento['Precio_Compra'] = obtener_precio_compra_medicamento()
                medicamento['Precio_Venta'] = obtener_precio_venta_medicamento()
                if medicamento['Precio_Venta'] <= medicamento['Precio_Compra']:
                    print('\nPrecio de venta invalido.\n')
                    return
                
                medicamento['Stock'] = obtener_stock_medicamento()
                medicamento['Stock_Minimo'] = obtener_stock_minimo_medicamento()
                if medicamento['Stock_Minimo'] > medicamento['Stock']:
                    print('\nStock minimo no puede ser mayor al stock del medicamento.\n')
                    return
                
                medicamento['Proveedor'] = obtener_proveedor_medicamento()
                
                guardar_medicamentos(medicamentos)
                print('\nMedicamento actualizado correctamente.\n')
                break
        if not encontrado:
            print('\nMedicamento no encontrado.\n')
    else:
        print('\nNo hay medicamentos registrados.\n')


# =======================================================================================
#                              ELIMINAR MEDICAMENTO                    
# =======================================================================================
def eliminar_medicamento():
    if medicamentos:
        encontrado = False
        nombre_medicamento_buscado = obtener_nombre_medicamento()

        for medicamento in medicamentos:
            if medicamento['Nombre'] == nombre_medicamento_buscado:
                encontrado = True
                print('\nMedicamento encontrado.\n')
                mostrar_medicamento(medicamento)

                medicamentos.remove(medicamento)
                guardar_medicamentos(medicamentos)
                print('\nMedicamento eliminado correctamente.\n')
                break
        if not encontrado:
            print('\nMedicamento no encontrado.\n')

    else:
        print('\nNo hay medicamentos registrados.\n')

# =======================================================================================
#                               MENU DE MEDICAMENTOS
# =======================================================================================
def menu_medicamentos():

    while True:
        mostrar_menu()

        try:
            opcion = int(input('Elija una opcion: '))

        except ValueError:
            print('\nDato invalido.\n')
            continue
        
        limpiar_consola()

        if opcion == 1:
            registrar_medicamento()

        elif opcion == 2:
            mostrar_medicamentos()

        elif opcion == 3:
            buscar_medicamento()

        elif opcion == 4:
            actualizar_medicamento()

        elif opcion == 5:
            eliminar_medicamento()

        elif opcion == 6:
            print('\nVolviendo al menu principal.\n')
            break

        else:
            print('\nOpcion invalida.\n')

