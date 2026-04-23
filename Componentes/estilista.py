# from Componentes.horario import Horario
from usuarios import Usuario
from servicio import Servicio


class Estilista(Usuario):

    def __init__(self, nombre, apellido, correo, telefono, especialidad=None, estado=None, horario=None):
        super().__init__(nombre, apellido, correo, telefono)
        self.especialidad = especialidad
        self.estado = estado
        self.horario = [] 
        self.agenda = []
        self.servicios = [] 

    def crear_estilista(self):
        print("\n|===| Crear Estilista |===|")

        self.crear_usuario()

        self.especialidad = input("Ingrese la especialidad: ")
        self.estado = input("Ingrese el estado (Disponible/Ocupado): ")

        print("\n--- Crear Horario ---")
        id_horario = input("ID del horario: ")
        hora_inicio = input("Hora inicio (ej: 08:00): ")
        hora_fin = input("Hora fin (ej: 18:00): ")
        dias = input("Días (separados por coma): ").split(",")

        self.horario = Horario(id_horario, hora_inicio, hora_fin, dias)

    def ver_agenda(self):
        print("\n|===| Agenda del estilista |===|")
        if not self.agenda:
            print("No hay citas registradas")
        else:
            for cita in self.agenda:
                print(f"{cita.fecha} - {cita.hora} - {cita.estado}")

    def agregar_cita(self, cita):
        self.agenda.append(cita)

    def obtener_horas_disponibles(self, fecha):
        if not self.horario:
            return []

        horas = self.horario.generar_horas_disponibles()

        # eliminar horas ocupadas
        for cita in self.agenda:
            if cita.fecha == fecha and cita.hora in horas:
                horas.remove(cita.hora)

        return horas

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)
        print(f"Servicio '{servicio.nombre}' agregado al estilista")

    def ver_servicios(self):
        print("\n|===| Servicios del Estilista |===|")
        if not self.servicios:
            print("No tiene servicios asignados")
        else:
            for s in self.servicios:
                print(f"- {s.nombre} (${s.precio})")

    def cambiar_estado(self):
        self.estado = input("Nuevo estado (Disponible/Ocupado): ")

    def ver_horario(self):
        if self.horario:
            self.horario.mostrar_horario()
        else:
            print("No hay horario asignado")

    def leer_usuario(self):
        super().leer_usuario()
        print(f"Especialidad: {self.especialidad}")
        print(f"Estado: {self.estado}")

        if self.horario:
            self.horario.mostrar_horario()
        else:
            print("Horario: No asignado")

        self.ver_servicios()