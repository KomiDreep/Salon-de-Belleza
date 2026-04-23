import estilista as Estilis
import servicio
import usuarios as User
import horario as Horario

class Cita:
    def __init__(self):
        self.lista_estilistas = []
        self.lista_servicios = []
        self.lista_usuarios = []

    def crear_estilista(self):

        print("\n|===| Crear Estilista |===|")
        print("Crear nuevo usuario")
        self.nombre = input("Ingrese el nombre del nuevo usuario: ")
        self.apellido = input("Ingrese el apellido del nuevo usuario: ")
        self.correo = input("Ingrese el correo del nuevo usuario: ")
        self.telefono = input("Ingrese el telefono del nuevo usuario: ")
        self.especialidad = input("Ingrese la especialidad: ")
        self.estado = input("Ingrese el estado (Disponible/Ocupado): ")
        estilista= Estilis.Estilista(self.nombre, self.apellido, self.correo, self.telefono, self.especialidad, self.estado)
        self.lista_estilistas.append(estilista)

    def editar_estilista(self):
        print("\n|===| Editar Estilista |===|")
        nombre = input("Ingrese el nombre del estilista a editar: ")

    for estilista in self.lista_estilistas:
        if estilista.nombre == nombre:
            print("Estilista encontrado. Ingrese los nuevos datos (deje vacío para no cambiar):")

            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_apellido = input("Nuevo apellido: ")
            nuevo_correo = input("Nuevo correo: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            nueva_especialidad = input("Nueva especialidad: ")
            nuevo_estado = input("Nuevo estado: ")

            if nuevo_nombre:
                estilista.nombre = nuevo_nombre
            if nuevo_apellido:
                estilista.apellido = nuevo_apellido
            if nuevo_correo:
                estilista.correo = nuevo_correo
            if nuevo_telefono:
                estilista.telefono = nuevo_telefono
            if nueva_especialidad:
                estilista.especialidad = nueva_especialidad
            if nuevo_estado:
                estilista.estado = nuevo_estado

            print("Estilista actualizado correctamente.")
            return

    print("Estilista no encontrado.")

    def eliminar_estilista(self):
        print("\n|===| Eliminar Estilista |===|")
        nombre = input("Ingrese el nombre del estilista a eliminar: ")

        for estilista in self.lista_estilistas:
            if estilista.nombre == nombre:
                self.lista_estilistas.remove(estilista)
                print("Estilista eliminado correctamente.")
                return

    print("Estilista no encontrado.")

    def crear_servicio(self):
        print("\n|===| Crear Servicio |===|")

        self.id_servicio = input("ID del servicio: ")
        self.nombre = input("Nombre del servicio: ")
        self.precio = float(input("Precio: "))
        self.duracion = int(input("Duración (minutos): "))
        self.descripcion = input("Descripción: ")
        nuevo_servicio= servicio.Servicio(self.id_servicio, self.nombre, self.precio, self.duracion, self.descripcion)
        self.lista_servicios.append(nuevo_servicio)

    def crear_usuario(self):
        print("Crear nuevo usuario")
        self.nombre = input("Ingrese el nombre del nuevo usuario: ")
        self.apellido = input("Ingrese el apellido del nuevo usuario: ")
        self.correo = input("Ingrese el correo del nuevo usuario: ")
        self.telefono = input("Ingrese el telefono del nuevo usuario: ")
        usuario= User.Usuario(self.nombre, self.apellido, self.correo, self.telefono)
        self.lista_usuarios.append(usuario)

    def crear_horario_estilista(self):
        nombre=input("Ingrese el nombre del estilista para asignar horario: ")
        estilista_encontrado = False
        for estilista in self.lista_estilistas:
            if estilista.nombre == nombre:
                estilista_encontrado = True
        if not estilista_encontrado:
            print("Estilista no encontrado")
            return

        print("\n--- Crear Horario ---")
        id_horario = input("ID del horario: ")
        hora_inicio = input("Hora inicio (ej: 08:00): ")
        hora_fin = input("Hora fin (ej: 18:00): ")
        dias = input("Días (separados por coma): ").split(",")
        horario= Horario(id_horario, hora_inicio, hora_fin, dias)
        estilista.horario.append(horario)
       
            
    
    def menu(self):
        while True:
            print("\n|===| Menú de Citas |===|")
            print("1. Crear Estilista")
            print("2. Crear Servicio")
            print("3. Crear Usuario")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_estilista()
            elif opcion == "2":
                self.editar_estilista()
            elif opcion == "3":
                self.eliminar_estilista()
            elif opcion == "4":
                self.crear_servicio()
            elif opcion == "5":
                self.crear_usuario()
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    cita = Cita()
    cita.menu()

  
