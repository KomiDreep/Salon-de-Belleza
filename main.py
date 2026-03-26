from Componentes.usuarios import usuario
from Componentes.estilista import Estilista
from Componentes.administrador import Administrador

admin1 = Administrador(1,"Carlos","Lopez","300123","Bogota")
estilista1 = Estilista(2,"Ana","Perez","301555","Bogota","Corte","Disponible")

admin1.leer_usuario()
admin1.crear_servicio()

print()

estilista1.leer_usuario()
estilista1.ver_agenda()