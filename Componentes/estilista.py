from Componentes.usuarios import Usuario

class Estilista(Usuario):

    def __init__(self, nombre, apellido, correo, telefono, especialidad, estado, horario):
        super().__init__(nombre, apellido, correo, telefono)
        self.especialidad = especialidad
        self.estado = estado
        self.horario = horario
        self.agenda = []  # lista de citas (para después)

    def crear_estilista(self):
        print("\n|===| Crear Estilista |===|")

        # reutilizamos datos de usuario
        self.crear_usuario()

        # datos propios
        self.especialidad = input("Ingrese la especialidad: ")
        self.estado = input("Ingrese el estado (Disponible/Ocupado): ")
        self.horario = input("Ingrese el horario (ej: 8am-6pm): ")

    def ver_agenda(self):
        print("\n|===| Agenda del estilista |===|")
        if not self.agenda:
            print("No hay citas registradas")
        else:
            for cita in self.agenda:
                print(cita)

    def cambiar_estado(self):
        self.estado = input("Nuevo estado (Disponible/Ocupado): ")

    def leer_usuario(self):
        super().leer_usuario()
        print(f"Especialidad: {self.especialidad}")
        print(f"Estado: {self.estado}")
        print(f"Horario: {self.horario}")