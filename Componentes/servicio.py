class Servicio:

    def __init__(self, id_servicio=None, nombre=None, precio=0, duracion=0, descripcion=""):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.precio = precio
        self.duracion = duracion  # en minutos
        self.descripcion = descripcion


    def mostrar_servicio(self):
        print("\n|===| Servicio |===|")
        print(f"ID: {self.id_servicio}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Duración: {self.duracion} minutos")
        print(f"Descripción: {self.descripcion}")