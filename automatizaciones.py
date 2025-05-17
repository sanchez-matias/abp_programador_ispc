def activar_modo_fiesta(dispositivos):
    for dispositivo in dispositivos:
        if dispositivo["tipo"] in [2, 3]:  # 2: luces, 3: música
            dispositivo["estado"] = True
    print("Modo Fiesta activado: luces y equipos de música encendidos.")

def apagar_modo_fiesta(dispositivos):
    for dispositivo in dispositivos:
        if dispositivo["tipo"] in [2, 3]:  # 2: luces, 3: música
            dispositivo["estado"] = False    