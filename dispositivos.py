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

def eliminar_dispositivo(nombre, confirmar, lista_dispositivos):
    for dispositivo in lista_dispositivos:
        if dispositivo["nombre"].lower() == nombre.lower():
            if confirmar.lower() == "si":
                lista_dispositivos.remove(dispositivo)
                return f"El dispositivo '{nombre}' fue eliminado."
            elif confirmar.lower() == "no":
                return "Operación cancelada..."
            else:
                return "Error: Solamente escriba 'si' o 'no'."
    return f"No se encontr ningun dispositivo llamado '{nombre}'."


def listar_dispositivos(dispositivos: list):
    for i in range(len(dispositivos)):
        print(f'{i}) {dispositivos[i]["nombre"]}')
