def buscar_por_nombre(nombre, lista):
    for i in lista:
        if nombre == i["nombre"]:
            return True
    
    return False

def agregar_dispositivo(dispositivos: list, nombre, tipo, estado):
    if not buscar_por_nombre(nombre, dispositivos):
        dispositivos.append({
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado,
        })

        return True

    return False

def listar_dispositivos(dispositivos: list):
    for i in range(len(dispositivos)):
        print(f'${i}) d{dispositivos[i]["nombre"]}')

def eliminar_dispositivo():
    pass