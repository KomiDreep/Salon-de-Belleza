class Usuario:

    contador_id = 1 

    def __init__(self,nombre, apellido, correo, telefono):
        self.id = Usuario.contador_id
        Usuario.contador_id += 1

        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def crear_usuario(self):
        print("Crear nuevo usuario")
        self.nombre = input("Ingrese el nombre del nuevo usuario: ")
        self.apellido = input("Ingrese el apellido del nuevo usuario: ")
        self.correo = input("Ingrese el correo del nuevo usuario: ")
        self.telefono = input("Ingrese el telefono del nuevo usuario: ")

    def leer_usuario(self):
        print(f"\n Información del usuario")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Correo: {self.correo}")
        print(f"Telefono: {self.telefono}")
    
    def actualizar_usuario(self):
        self.nombre = input("Ingrese el nuevo nombre del usuario: ")
        self.apellido = input("Ingrese el nuevo apellido del usuario: ")
        self.correo = input("Ingrese el nuevo correo del usuario: ")
        self.telefono = input("Ingrese el nuevo telefono del usuario: ")

    def eliminar_usuario(self, lista_usuarios):
        id_buscar = int(input("Ingrese ID del usuario a eliminar: "))

        for u in lista_usuarios:
            if u.id == id_buscar:
                lista_usuarios.remove(u)
                print("Usuario eliminado correctamente")
                return

    print("Usuario no encontrado")

if __name__ == "__main__":

    lista_usuarios = []

    print("=== CREAR USUARIO 1 ===")
    usuario1 = Usuario("", "", "", "")
    usuario1.crear_usuario()
    lista_usuarios.append(usuario1)

    print("\n=== CREAR USUARIO 2 ===")
    usuario2 = Usuario("", "", "", "")
    usuario2.crear_usuario()
    lista_usuarios.append(usuario2)

    print("\n=== LISTA ACTUAL ===")
    for u in lista_usuarios:
        u.leer_usuario()

    print("\n=== ELIMINAR USUARIO ===")
    usuario1.eliminar_usuario(lista_usuarios)

    print("\n=== LISTA FINAL ===")
    for u in lista_usuarios:
        u.leer_usuario()