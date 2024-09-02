class Cancha:
    #Clase que define las canchas y sus atributos
    def __init__(self, id_cancha, tipo, disponible=True, con_luz=False, horario_reservado=None, duracion_reserva=1):
        self.id_cancha = id_cancha
        self.tipo = tipo
        self.disponible = disponible
        self.con_luz = con_luz
        self.horario_reservado = horario_reservado
        self.duracion_reserva = duracion_reserva

    def calcular_horario_fin(self):
        # Se encarga de calcular el horario de finalización de la reserva
        if self.horario_reservado:
            hora_inicio, _ = map(int, self.horario_reservado.split(":"))
            hora_fin = (hora_inicio + self.duracion_reserva) % 24
            return f"{hora_fin:02}:00"
        return None

    def __str__(self):
        # Se encarga de devolver el estado de la cancha como una cadena de texto
        if self.disponible:
            estado = "Disponible"
        else:
            horario_fin = self.calcular_horario_fin()
            estado = f"Ocupado (Reservada de {self.horario_reservado} a {horario_fin})"
        luz = "con luz" if self.con_luz else ""
        return f"Cancha {self.id_cancha}: {self.tipo} - {estado} {luz}".strip()

class SistemaReservas:
    def __init__(self):
        # Se encarga de inicializar las canchas disponibles y las reservas
        self.canchas = [
            Cancha(1, "Básquet"), Cancha(2, "Básquet"),
            Cancha(3, "Vóley"), Cancha(4, "Vóley"),
            Cancha(5, "Tenis"), Cancha(6, "Tenis"),
            Cancha(7, "Pádel"), Cancha(8, "Pádel"),
            Cancha(9, "Pádel"), Cancha(10, "Pádel"),
            Cancha(11, "Fútbol 5"), Cancha(12, "Fútbol 5")
        ]
        self.reservas = []

    def mostrar_canchas_por_horario(self, horario):
        # Se encarga de mostrar todas las canchas y su disponibilidad para un horario específico
        for cancha in self.canchas:
            print(cancha)

    def mostrar_canchas_ocupadas(self):
        # Se encarga de mostrar las canchas que están ocupadas
        canchas_ocupadas = [c for c in self.canchas if not c.disponible]
        if canchas_ocupadas:
            print("\nCanchas ocupadas:")
            for cancha in canchas_ocupadas:
                print(cancha)
        else:
            print("No hay canchas ocupadas en este momento.")

    def reservar_cancha(self, id_cancha, horario, duracion=1, con_luz=False):
        # Se encarga de realizar una reserva
        cancha = next((c for c in self.canchas if c.id_cancha == id_cancha), None)
        if cancha and cancha.disponible:
            cancha.disponible = False
            cancha.con_luz = con_luz
            cancha.horario_reservado = horario
            cancha.duracion_reserva = duracion
            self.reservas.append(cancha)
            hora_fin = cancha.calcular_horario_fin()
            luz = "con luz" if con_luz else ""
            print(f"Reserva exitosa para {cancha.tipo} (ID: {id_cancha}) de {horario} a {hora_fin} {luz}")
        else:
            print("Cancha no disponible o inexistente.")

    def liberar_cancha(self, id_cancha):
        # Se encarga de anular una reserva
        cancha = next((c for c in self.canchas if c.id_cancha == id_cancha), None)
        if cancha and not cancha.disponible:
            cancha.disponible = True
            cancha.con_luz = False
            cancha.horario_reservado = None
            cancha.duracion_reserva = 1
            self.reservas.remove(cancha)
            print(f"La cancha {id_cancha} ha sido liberada.")
        else:
            print("Cancha ya está disponible o no existe.")

    def horario_valido(self, horario):
        # Se encarga de verificar si el horario ingresado es válido según el horario de apertura del predio
        try:
            hora, minutos = map(int, horario.split(":"))
            if (13 <= hora < 24) or (0 <= hora <= 2):
                return True
            return False
        except ValueError:
            return False
