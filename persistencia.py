# =======================================================================================
#                                  PERSISTENCIA DE LOS DATOS    
# =======================================================================================

# =======================================================================================
#                               FUNCIONES Y MODULOS IMPORTADOS   
# =======================================================================================
import json
import os

# =======================================================================================
#                             GUARDAR MEDICAMENTOS EN .JSON        
# =======================================================================================
def guardar_medicamentos(medicamentos):
    ruta = os.path.join(
        os.path.dirname(__file__),
        'datos',
        'medicamentos.json'
    )

    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(
            medicamentos,
            archivo,
            indent=4,
            ensure_ascii=False
        )

# =======================================================================================
#                             CARGAR MEDICAMENTOS EN .JSON        
# =======================================================================================
def cargar_medicamentos():
    ruta = os.path.join(
        os.path.dirname(__file__),
        'datos',
        'medicamentos.json'
    )
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# =======================================================================================
#                            GUARDAD PROVEEDORES EN JSON     
# =======================================================================================
def guardar_proveedores(proveedores):
    ruta = os.path.join(
        os.path.dirname(__file__),
        'datos',
        'proveedores.json'
    )
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(
            proveedores,
            archivo,
            indent=4,
            ensure_ascii=False
        )

# =======================================================================================
#                          CARGAR PROVEEDORES EN JSON       
# =======================================================================================
def cargar_proveedores():
    ruta = os.path.join(
        os.path.dirname(__file__),
        'datos',
        'proveedores.json'
    )
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []    

# =======================================================================================
#                              GUARDAD EMPLEADOS EN JSON   
# =======================================================================================
def guardar_empleados(empleados):
    ruta = os.path.join(
        os.path.dirname(__file__),
        'datos',
        'empleados.json'
    )
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(
            empleados,
            archivo,
            indent=4,
            ensure_ascii=False
        )

# =======================================================================================
#                               CARGAR EMPLEADOS EN EL JSON               
# =======================================================================================
def cargar_empleados():
    ruta = os.path.join(
        os.path.dirname(__file__),
        'datos',
        'empleados.json'
    )
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
# =======================================================================================
#                                 GUARDAR CLIENTES EN EL JSON
# =======================================================================================
def guardar_clientes(clientes):
    ruta = os.path.join(
        os.path.dirname(__file__),
        'datos',
        'clientes.json'
    )
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(
            clientes,
            archivo,
            indent=4,
            ensure_ascii=False
        )
# =======================================================================================
#                                   CARGAR CLIENTES EN EL JSON          
# =======================================================================================
def cargar_clientes():
    ruta = os.path.join(
        os.path.dirname(__file__),
        'datos',
        'clientes.json'
    )
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# =======================================================================================
#                                 GUARDAR VENTAS EN EL JSON 
# =======================================================================================
def guardar_ventas(ventas):
    ruta = os.path.join(
        os.path.dirname(__file__),
        'datos',
        'ventas.json'
    )
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(
            ventas,
            archivo,
            indent=4,
            ensure_ascii=False
        )     
    
# =======================================================================================
#                                 CARGAR VENTAS EN EL JSON
# =======================================================================================
def cargar_ventas():
    ruta = os.path.join(
        os.path.dirname(__file__),
        'datos',
        'ventas.json'
    )
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

