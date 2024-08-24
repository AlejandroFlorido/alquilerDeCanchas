from models import SistemaReservas

def mostrar_menu():
    print("\n--- Sistema de Alquiler de Canchas ---")
    print("1. Reservar una cancha")
    print("2. Liberar una cancha")
    print("3. Ver todas las canchas")
    print("4. Salir")

def mostrar_canchas(sistema):
    print("\nCanchas disponibles y ocupadas:")
    for cancha in sistema.canchas:
        print(cancha)  # Usa el método __str__ de la clase Cancha para mostrar la información

def main():
    sistema = SistemaReservas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            horario = input("Ingresa el horario de la reserva (HH:MM): ")
            if sistema.horario_valido(horario):
                duracion = int(input("¿Por cuántas horas deseas reservar la cancha?: "))
                mostrar_canchas(sistema)
                id_cancha = int(input("\nIngresa el ID de la cancha que deseas reservar: "))
                con_luz = input("¿Deseas alquilar la cancha con luz? (s/n): ").strip().lower()
                con_luz = con_luz == "s"
                sistema.reservar_cancha(id_cancha, horario, duracion, con_luz)
            else:
                print("Horario no válido. El predio está abierto de 13:00 a 02:00.")
        elif opcion == "2":
            id_cancha = int(input("Ingresa el ID de la cancha a liberar: "))
            sistema.liberar_cancha(id_cancha)
        elif opcion == "3":
            mostrar_canchas(sistema)
        elif opcion == "4":
            print("Gracias por utilizar el sistema de reservas del Grupo n5!!!")
            print("Hasta luego!!!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
