# src/models.py

class Cancha:
    def __init__(self, id_cancha, tipo, disponible=True, con_luz=False, horario_reservado=None):
        self.id_cancha = id_cancha
        self.tipo = tipo
        self.disponible = disponible
        self.con_luz = con_luz
        self.horario_reservado = horario_reservado

    def __str__(self):
        estado = "Disponible" if self.disponible else f"Ocupado (Reservada a las {self.horario_reservado})"
        luz = "con luz" if self.con_luz else ""
        return f"Cancha {self.id_cancha}: {self.tipo} - {estado} {luz}".strip()

class SistemaReservas:
    def __init__(self):
        self.canchas = [
            Cancha(1, "Básquet"), Cancha(2, "Básquet"),
            Cancha(3, "Vóley"), Cancha(4, "Vóley"),
            Cancha(5, "Tenis"), Cancha(6, "Tenis"),
            Cancha(7, "Pádel"), Cancha(8, "Pádel"),
            Cancha(9, "Pádel"), Cancha(10, "Pádel"),
            Cancha(11, "Fútbol 5"), Cancha(12, "Fútbol 5")
        ]
        self.reservas = []

    #Muestra todas las canchas y muestra su disponibilidad para un horario específico.
    def canchas_disponibles_por_horario(self, horario):
        disponibles_y_ocupadas = [c for c in self.canchas if c.horario_reservado == horario or c.disponible]
        return disponibles_y_ocupadas

    def reservar_cancha(self, id_cancha, horario, con_luz=False):
        cancha = next((c for c in self.canchas if c.id_cancha == id_cancha), None)
        if cancha and cancha.disponible:
            cancha.disponible = False
            cancha.con_luz = con_luz
            cancha.horario_reservado = horario
            self.reservas.append(cancha)
            luz = "con luz" if con_luz else ""
            print(f"Reserva exitosa para {cancha.tipo} (ID: {id_cancha}) a las {horario} {luz}")
        else:
            print("Cancha no disponible o inexistente.")

    def liberar_cancha(self, id_cancha):
        cancha = next((c for c in self.canchas if c.id_cancha == id_cancha), None)
        if cancha and not cancha.disponible:
            cancha.disponible = True
            cancha.con_luz = False
            cancha.horario_reservado = None
            self.reservas.remove(cancha)
            print(f"La cancha {id_cancha} ha sido liberada.")
        else:
            print("Cancha ya está disponible o no existe.")

    def horario_valido(self, horario):
        try:
            hora, minutos = map(int, horario.split(":"))
            if (13 <= hora < 24) or (0 <= hora <= 2):
                return True
            return False
        except ValueError:
            return False
