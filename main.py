import dispositivos
import automatizaciones

"""
{
    "nombre": <string>,
    "tipo": <int>,
    "estado": <bool>
}
"""

lista_dispositivos = [
    {"nombre": 'Luces', "tipo": 2, "estado": True},
    {"nombre": 'Camara seguridad', "tipo": 1, "estado": False},
    {"nombre": 'Equipo musica', "tipo": 3, "estado": True},
    {"nombre": 'Luces 2', "tipo": 2, "estado": True}
]

def imprimirEstado():
    for dispositivo in lista_dispositivos:
        print(dispositivo)

if __name__ == '__main__':
    while True:
        print("--- MENU PRINCIPAL ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Modificar Modo Fiesta")
        print("6. Modificar Modo Noche")
        print("7. Salir")
        opcion = input("Seleccione una de las opciones: ")
        print ("-------------------------------------------")

        if opcion == "1":
            nombre = input("Nombre del nuevo dispositivo: ")
            tipo = int(input("Tipo (numero 1, 2, 3): "))
            estado = input("¿Está activo? (si/no): ")
            if dispositivos.agregar_dispositivo(lista_dispositivos, nombre, tipo, estado):
                print("El dispositivo ingresado se registro con exito.")
            else:
                print("Ya existe un dispositivo con ese nombre. Vuelva a intentarlo con otro")

        elif opcion == "2":
            dispositivos.listar_dispositivos(lista_dispositivos)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del dispositivo a buscar: ")
            if dispositivos.buscar_por_nombre(nombre, lista_dispositivos):
                print(f"El dispositivo ingresado como '{nombre}' si existe.")
            else:
                print(f"No existe ningun dispositivo llamado '{nombre}'.")

        elif opcion == "4":
            dispositivo = input("Ingrese el dispositivo que quiere eliminar: ")
            confirmar = input(f"¿Esta seguro que desea eliminar el dispositivo '{dispositivo}'? (si/no): ")
            print(dispositivos.eliminar_dispositivo(dispositivo, confirmar, lista_dispositivos))

        elif opcion == "5":
            accion = int(input("Ingrese 1 para encender el modo fiesta y 2 para apagarlo: "))
            if accion == 1:
                print(automatizaciones.activar_modo_fiesta(lista_dispositivos))
            elif accion == 2:
                print(automatizaciones.apagar_modo_fiesta(lista_dispositivos))
            else:
                print("opcion no validad")        
        elif opcion == "6":
            accion = int(input("Ingrese 1 para encender el modo noche y 2 para apagarlo: "))
            if accion == 1:
                print(automatizaciones.activar_modo_noche(lista_dispositivos))
            elif accion == 2:
                print(automatizaciones.apagar_modo_noche(lista_dispositivos))
            else:
                print("opcion no validad")
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        imprimirEstado()    