
"""
{
    "nombre": <string>,
    "tipo": <int>,
    "estado": <bool>
}
"""

dispositivos = [
    {
        "nombre": 'Nikonasd asda',
        "tipo": 2,
        "estado": False,
    },
]

if __name__ == '__main__':
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Activar Modo Fiesta")
        print("6. Activar Modo Noche")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_dispositivo()
        elif opcion == "2":
            listar_dispositivos()
        elif opcion == "3":
            buscar_dispositivo()
        elif opcion == "4":
            eliminar_dispositivo()
        elif opcion == "5":
            activar_modo_fiesta(dispositivos)
        elif opcion == "6":
            activar_modo_noche(dispositivos)
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

        