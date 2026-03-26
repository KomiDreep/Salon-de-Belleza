from Componentes.usuarios import Usuario
from Componentes.estilista import Estilista

class Administrador(Usuario):

    def __init__(self, nombre, apellido, correo, telefono):
        super().__init__(nombre, apellido, correo, telefono)

    #Usuarios

    def crear_usuario_sistema(self, lista_usuarios):
        print("\n|===| Crear Usuario |===|")
        nuevo = Usuario("", "", "", "")
        nuevo.crear_usuario()
        lista_usuarios.append(nuevo)
        print("Usuario creado correctamente")

    def ver_usuarios(self, lista_usuarios):
        print("\n|===| Lista de Usuarios |===|")
        if not lista_usuarios:
            print("No hay usuarios registrados")
            return

        for u in lista_usuarios:
            u.leer_usuario()
            print("-----------")

    def actualizar_usuario_sistema(self, lista_usuarios):
        id_buscar = int(input("Ingrese ID del usuario a actualizar: "))

        for u in lista_usuarios:
            if u.id == id_buscar:
                u.actualizar_usuario()
                print("Usuario actualizado correctamente")
                return

        print("Usuario no encontrado")

    def eliminar_usuario(self, lista_usuarios):
        id_buscar = int(input("Ingrese ID del usuario a eliminar: "))

        for u in lista_usuarios:
            if u.id == id_buscar:
                lista_usuarios.remove(u)
                print("Usuario eliminado correctamente")
                return

        print("Usuario no encontrado")

    #Estilistas

    def crear_estilista(self, lista_estilistas):
        print("\n|===| Crear Estilista |===|")
        nuevo = Estilista("", "", "", "", "", "", "")
        nuevo.crear_estilista()
        lista_estilistas.append(nuevo)
        print("Estilista creado correctamente")

    def ver_estilistas(self, lista_estilistas):
        print("\n|===| Lista de Estilistas |===|")
        if not lista_estilistas:
            print("No hay estilistas registrados")
            return

        for e in lista_estilistas:
            e.leer_usuario()
            print("-----------")

    def actualizar_estilista(self, lista_estilistas):
        id_buscar = int(input("Ingrese ID del estilista a actualizar: "))

        for e in lista_estilistas:
            if e.id == id_buscar:
                e.crear_estilista()  # reutilizamos método
                print("Estilista actualizado correctamente")
                return

        print("Estilista no encontrado")

    def eliminar_estilista(self, lista_estilistas):
        id_buscar = int(input("Ingrese ID del estilista a eliminar: "))

        for e in lista_estilistas:
            if e.id == id_buscar:
                lista_estilistas.remove(e)
                print("Estilista eliminado correctamente")
                return

        print("Estilista no encontrado")