cuentas = {
    "Juan Perez": {"contraseña": "1234"},
    "Ana Lopez": {"contraseña": "5678"},
    "Carlos Gomez": {"contraseña": "abcd"}
}

def listar_usuario():
    if not cuentas:
        return "No hay usuarios registrados."
    return list(cuentas.keys())

def buscar_usuario(usuario):
    if usuario in cuentas:
        return f"El usuario '{usuario}' fue encontrado con exito"
    return f"Error: El usuario '{usuario}' no esta registrado. Revisa que lo escribiste correctamente."

def eliminar_usuario(usuario, confirmar):
    if usuario in cuentas:
        if confirmar.lower() == 'si':
            cuentas.pop(usuario)
            return f"El usuario '{usuario}' fue removido con éxito."
        elif confirmar.lower() == 'no':
            return "Operación cancelada."
        else:
            return "Error: respuesta inválida. Escriba 'si' o 'no'."
    return f"Error: El usuario '{usuario}' no fue encontrado."

def registrar_usuario(usuario, contraseña):
    if usuario in cuentas:
        return f"Error: El usuario '{usuario}' ya esta registrado."
    cuentas[usuario] = {"contraseña": contraseña}
    return f"Usuario '{usuario}' registrado correctamente."