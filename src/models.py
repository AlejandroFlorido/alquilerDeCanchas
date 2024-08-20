# src/models.py

class Cancha:
    def __init__(self, id_cancha, tipo, disponible=True):
        self.id_cancha = id_cancha
        self.tipo = tipo
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Cancha {self.id_cancha}: {self.tipo} - {estado}"


class SistemaReservas:
    def __init__(self):
        # Crear las canchas disponibles
        self.canchas = [
            Cancha(1, "Básquet"), Cancha(2, "Básquet"),
            Cancha(3, "Vóley"), Cancha(4, "Vóley"),
            Cancha(5, "Tenis"), Cancha(6, "Tenis"),
            Cancha(7, "Pádel"), Cancha(8, "Pádel"),
            Cancha(9, "Pádel"), Cancha(10, "Pádel"),
            Cancha(11, "Fútbol 5"), Cancha(12, "Fútbol 5")
        ]
        self.reservas = []

    def mostrar_canchas_disponibles(self):
        disponibles = [cancha for cancha in self.canchas if cancha.disponible]
        for cancha in disponibles:
            print(cancha)

    def reservar_cancha(self, id_cancha):
        cancha = next((c for c in self.canchas if c.id_cancha == id_cancha), None)
        if cancha and cancha.disponible:
            cancha.disponible = False
            self.reservas.append(cancha)
            print(f"Reserva exitosa para {cancha}")
        else:
            print("Cancha no disponible o inexistente.")

    def liberar_cancha(self, id_cancha):
        cancha = next((c for c in self.canchas if c.id_cancha == id_cancha), None)
        if cancha and not cancha.disponible:
            cancha.disponible = True
            self.reservas.remove(cancha)
            print(f"La cancha {id_cancha} ha sido liberada.")
        else:
            print("Cancha ya está disponible o no existe.")
