import streamlit as st

# Definimos la clase padre Empleado y sus atributos comunes
class Empleado:
    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni

    # Getter y Setter de Nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    # Getter y Setter de DNI
    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        self._dni = dni

    # Método para obtener un resumen del empleado
    def get_resumen(self):
        return f"{self.get_nombre()} - {self.__class__.__name__}"

    # Método para obtener el jefe inmediato (se sobreescribirá en las subclases)
    def get_jefe_inmediato(self):
        return "No asignado"

    # Método para obtener el estado del empleado
    def get_estado(self, estado):
        estados_validos = {"TC": "Término de contrato", "D": "Despido", "R": "Renuncia"}
        return estados_validos.get(estado, "Activo")

# Definimos la clase Gerente
class Gerente(Empleado):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self._subordinados = []

    def get_subordinados(self):
        return self._subordinados

    def set_subordinados(self, subordinados):
        self._subordinados = subordinados

    def agregar_subordinado(self, jefe):
        self._subordinados.append(jefe)

# Definimos la clase Jefe de Área
class JefeArea(Empleado):
    def __init__(self, nombre, dni, gerente):
        super().__init__(nombre, dni)
        self._gerente = gerente
        self._subordinados = []

    def get_jefe_inmediato(self):
        return self._gerente.get_nombre() if self._gerente else "No tiene jefe inmediato"
    
    def get_gerente(self):
        return self._gerente
    
    def set_gerente(self, gerente):
        self._gerente = gerente

    def agregar_subordinado(self, empleado):
        self._subordinados.append(empleado)

    def get_subordinados(self):
        return self._subordinados

    def set_subordinados(self, subordinados):
        self._subordinados = subordinados

# Definimos la clase Asistente
class Asistente(Empleado):
    def __init__(self, nombre, dni, jefe_area):
        super().__init__(nombre, dni)
        self._jefe_area = jefe_area

    def get_jefe_inmediato(self):
        return self._jefe_area.get_nombre() if self._jefe_area else "No tiene jefe inmediato"
    
    def get_jefe_area(self):
        return self._jefe_area
    
    def set_jefe_area(self, jefe_area):
        self._jefe_area = jefe_area

# Definimos la clase Técnico
class Tecnico(Empleado):
    def __init__(self, nombre, dni, jefe_area, anios_experiencia):
        super().__init__(nombre, dni)
        self._jefe_area = jefe_area
        self._anios_experiencia = anios_experiencia

    def get_jefe_inmediato(self):
        return self._jefe_area.get_nombre() if self._jefe_area else "No tiene jefe inmediato"

    def get_resumen(self):
        return f"{self.get_nombre()} - {self.__class__.__name__} - {self._anios_experiencia} años de experiencia"

    def get_anios_experiencia(self):
        return self._anios_experiencia

    def set_anios_experiencia(self, anios):
        self._anios_experiencia = anios

# Instanciar el Gerente
gerente = Gerente("Carlos López", "12345678")

# Crear los 5 jefes de área y asignarlos al gerente
jefes = [
    JefeArea("María Pérez", "87654321", gerente),
    JefeArea("Juan García", "56781234", gerente),
    JefeArea("Luis Torres", "34567812", gerente),
    JefeArea("Ana Mendoza", "23456789", gerente),
    JefeArea("Pedro Ruiz", "45678123", gerente)
]

for jefe in jefes:
    gerente.agregar_subordinado(jefe)

# Crear asistentes
asistentes = [
    Asistente("Ana Torres", "11111111", jefes[0]),
    Asistente("Luis Mendoza", "22222222", jefes[1]),
    Asistente("Sofía Herrera", "33333333", jefes[2]),
    Asistente("Carlos Ramírez", "44444444", jefes[3]),
    Asistente("Gabriela Núñez", "55555555", jefes[4])
]

# Crear técnicos
tecnicos = [
    Tecnico("José Fernández", "66666666", jefes[0], 4),
    Tecnico("Elena Ríos", "77777777", jefes[0], 2),
    Tecnico("Manuel Gómez", "88888888", jefes[1], 5),
    Tecnico("Clara Vidal", "99999999", jefes[1], 3),
    Tecnico("Ricardo Salas", "10101010", jefes[2], 1)
]

# Asignar subordinados
for asistente in asistentes:
    asistente.get_jefe_area().agregar_subordinado(asistente)

for tecnico in tecnicos:
    tecnico.get_jefe_area().agregar_subordinado(tecnico)

# Mostrar información con Streamlit
st.title("Sistema de Recursos Humanos - Business Corporation")

for empleado in [gerente] + jefes + asistentes + tecnicos:
    st.subheader(f"Nombre: {empleado.get_nombre()}")
    st.text(f"Resumen: {empleado.get_resumen()}")
    st.text(f"Jefe inmediato: {empleado.get_jefe_inmediato()}")
    st.text(f"Estado: {empleado.get_estado('Activo')}")
    
    if hasattr(empleado, 'get_subordinados') and empleado.get_subordinados():
        st.text("Subordinados:")
        for sub in empleado.get_subordinados():
            st.text(f"  - {sub.get_resumen()}")
    
    st.markdown("---")
