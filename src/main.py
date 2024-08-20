# src/main.py
from models import SistemaReservas

def mostrar_menu():
    print("\n--- Sistema de Alquiler de Canchas ---")
    print("1. Mostrar canchas disponibles")
    print("2. Reservar una cancha")
    print("3. Liberar una cancha")
    print("4. Salir")

def main():
    sistema = SistemaReservas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            sistema.mostrar_canchas_disponibles()
        elif opcion == "2":
            id_cancha = int(input("Ingresa el ID de la cancha a reservar: "))
            sistema.reservar_cancha(id_cancha)
        elif opcion == "3":
            id_cancha = int(input("Ingresa el ID de la cancha a liberar: "))
            sistema.liberar_cancha(id_cancha)
        elif opcion == "4":
            print("Gracias por utilizar nuestro sistema de reservas!")
            print("Los saluda cordialmente el grupo N°")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
