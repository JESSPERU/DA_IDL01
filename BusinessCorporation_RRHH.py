# Definimos la clase padre Empleado y sus atributos comunes
class Empleado:
    def __init__(self,nombre,dni):
        self.nombre=nombre
        self.dni=dni
    # Aplicamos los métodos para obtener información
    # Método para obtener un resumen del empleado
    def get_resumen(self):
        return(f"{self.nombre} - {self.__class__.__name__}")
    # Método para obtener el jefe inmediato (se sobreescribirá en las subclases)
    def get_jefe_inmediato(self):
        return "No asignado"
    # Método para obtener el estado del empleado
    def get_estado(self, estado):
        # Definimos los estados posibles
        estados_validos = {"TC": "Término de contrato", "D": "Despido", "R": "Renuncia"}
        return estados_validos.get(estado, "Activo")

# Definimos la clase Gerente que hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, dni):
        # Llamamos al constructor de la clase padre
        super().__init__(nombre, dni)
        self.subordinados = []  # Lista para almacenar a los jefes de área

    # Método para agregar jefes de área como subordinados
    def agregar_subordinado(self, jefe):
        self.subordinados.append(jefe)

# Definimos la clase Jefe de Área que hereda de Empleado
class JefeArea(Empleado):
    def __init__(self, nombre, dni, gerente):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, dni)
        self.gerente = gerente  # Asignamos el gerente como jefe inmediato
        self.subordinados = []  # Lista de asistentes y técnicos

    # Método para obtener el jefe inmediato
    def get_jefe_inmediato(self):
        return self.gerente.nombre if self.gerente else "No tiene jefe inmediato"

    # Método para agregar subordinados
    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)


# Definimos la clase Asistente que hereda de Empleado
class Asistente(Empleado):
    def __init__(self, nombre, dni, jefe_area):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, dni)
        self.jefe_area = jefe_area  # Asignamos el jefe de área como jefe inmediato

    # Método para obtener el jefe inmediato
    def get_jefe_inmediato(self):
        return self.jefe_area.nombre if self.jefe_area else "No tiene jefe inmediato"


# Definimos la clase Técnico que hereda de Empleado
class Tecnico(Empleado):
    def __init__(self, nombre, dni, jefe_area, anios_experiencia):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, dni)
        self.jefe_area = jefe_area  # Asignamos el jefe de área como jefe inmediato
        self.anios_experiencia = anios_experiencia  # Agregamos los años de experiencia

    # Método para obtener el jefe inmediato
    def get_jefe_inmediato(self):
        return self.jefe_area.nombre if self.jefe_area else "No tiene jefe inmediato"

    # Sobreescribimos el método get_resumen para incluir los años de experiencia
    def get_resumen(self):
        return f"{self.nombre} - {self.__class__.__name__} - {self.anios_experiencia} años de experiencia"

#Empezamos a instanciar para mostrar el código creado
# Instanciamos un gerente
gerente1 = Gerente("Carlos López", "12345678")

# Instanciamos jefes de área y los asignamos al gerente
jefe1 = JefeArea("María Pérez", "87654321", gerente1)
jefe2 = JefeArea("Juan García", "56781234", gerente1)

# Agregamos los jefes de área a la lista de subordinados del gerente
gerente1.agregar_subordinado(jefe1)
gerente1.agregar_subordinado(jefe2)

# Instanciamos asistentes y técnicos y los asignamos a jefes de área
asistente1 = Asistente("Ana Torres", "34567812", jefe1)
asistente2 = Asistente("Luis Mendoza", "23456789", jefe2)

tecnico1 = Tecnico("Pedro Ruiz", "45678123", jefe1, 5)
tecnico2 = Tecnico("Sofía Herrera", "67891234", jefe2, 3)

# Agregamos los asistentes y técnicos a las listas de subordinados de los jefes
jefe1.agregar_subordinado(asistente1)
jefe1.agregar_subordinado(tecnico1)

jefe2.agregar_subordinado(asistente2)
jefe2.agregar_subordinado(tecnico2)

# Creamos un array de empleados con todos los objetos creados
empleados = [gerente1, jefe1, jefe2, asistente1, asistente2, tecnico1, tecnico2]

# Recorremos la lista de empleados e imprimimos su resumen
for empleado in empleados:
    print(empleado.get_resumen())