class Horario:
    def __init__(self, id_horario, hora_inicio, hora_fin, dias):
        self.id_horario = id_horario
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.dias = dias

    def mostrar_horario(self):
        print("\n|===| Horario |===|")
        print(f"ID: {self.id_horario}")
        print(f"Hora inicio: {self.hora_inicio}")
        print(f"Hora fin: {self.hora_fin}")
        print(f"Días: {', '.join(self.dias)}")

    def generar_horas_disponibles(self):
        horas = []
        inicio = int(self.hora_inicio.split(":")[0])
        fin = int(self.hora_fin.split(":")[0])

        for h in range(inicio, fin):
            horas.append(f"{h:02d}:00")

        return horas