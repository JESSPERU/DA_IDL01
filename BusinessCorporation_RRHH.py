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
    def get_nombre(self):
        return self.nombre

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

# Instanciar el Gerente
gerente = Gerente("Carlos López", "12345678")

# Crear los 5 jefes de área y asignarlos al gerente
jefes = [
    JefeArea("María Pérez", "87654321", gerente),  # Marketing
    JefeArea("Juan García", "56781234", gerente),  # Sistemas
    JefeArea("Luis Torres", "34567812", gerente),  # Producción
    JefeArea("Ana Mendoza", "23456789", gerente),  # Logística
    JefeArea("Pedro Ruiz", "45678123", gerente)    # Finanzas
]

# Agregar los jefes al gerente
for jefe in jefes:
    gerente.agregar_subordinado(jefe)

# Crear asistentes (1 o 2 por jefe)
asistentes = [
    Asistente("Ana Torres", "11111111", jefes[0]),  # Marketing
    Asistente("Luis Mendoza", "22222222", jefes[1]),  # Sistemas
    Asistente("Sofía Herrera", "33333333", jefes[2]),  # Producción
    Asistente("Carlos Ramírez", "44444444", jefes[3]),  # Logística
    Asistente("Gabriela Núñez", "55555555", jefes[4])   # Finanzas
]

# Crear técnicos (3 a 5 por jefe)
tecnicos = [
    Tecnico("José Fernández", "66666666", jefes[0], 4),
    Tecnico("Elena Ríos", "77777777", jefes[0], 2),
    Tecnico("Manuel Gómez", "88888888", jefes[1], 5),
    Tecnico("Clara Vidal", "99999999", jefes[1], 3),
    Tecnico("Ricardo Salas", "10101010", jefes[2], 1),
    Tecnico("Andrea Castro", "11111112", jefes[3], 2),
    Tecnico("Daniel Peralta", "12121212", jefes[4], 3)
]

# Asignar asistentes y técnicos a los jefes correspondientes
for asistente in asistentes:
    asistente.jefe_area.agregar_subordinado(asistente)

for tecnico in tecnicos:
    tecnico.jefe_area.agregar_subordinado(tecnico)

# Crear el array de empleados
empleados = [gerente] + jefes + asistentes + tecnicos

for empleado in empleados:
    print(f"Nombre: {empleado.nombre}")
    print(f"Resumen: {empleado.get_resumen()}")
    print(f"Jefe inmediato: {empleado.get_jefe_inmediato()}")
    print(f"Estado: {empleado.get_estado('Activo')}")
    print("-" * 30)  # Separador

