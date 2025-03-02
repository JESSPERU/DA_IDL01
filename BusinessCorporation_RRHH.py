import streamlit as st

# Definimos la clase padre Empleado y sus atributos comunes
class Empleado:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def get_resumen(self):
        return f"{self.nombre} - {self.__class__.__name__}"

    def get_jefe_inmediato(self):
        return "No asignado"

    def get_estado(self, estado):
        estados_validos = {"TC": "Término de contrato", "D": "Despido", "R": "Renuncia"}
        return estados_validos.get(estado, "Activo")

class Gerente(Empleado):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self.subordinados = []

    def agregar_subordinado(self, jefe):
        self.subordinados.append(jefe)

class JefeArea(Empleado):
    def __init__(self, nombre, dni, gerente):
        super().__init__(nombre, dni)
        self.gerente = gerente
        self.subordinados = []

    def get_jefe_inmediato(self):
        return self.gerente.nombre if self.gerente else "No tiene jefe inmediato"

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

class Asistente(Empleado):
    def __init__(self, nombre, dni, jefe_area):
        super().__init__(nombre, dni)
        self.jefe_area = jefe_area

    def get_jefe_inmediato(self):
        return self.jefe_area.nombre if self.jefe_area else "No tiene jefe inmediato"

class Tecnico(Empleado):
    def __init__(self, nombre, dni, jefe_area, anios_experiencia):
        super().__init__(nombre, dni)
        self.jefe_area = jefe_area
        self.anios_experiencia = anios_experiencia

    def get_jefe_inmediato(self):
        return self.jefe_area.nombre if self.jefe_area else "No tiene jefe inmediato"

    def get_resumen(self):
        return f"{self.nombre} - {self.__class__.__name__} - {self.anios_experiencia} años de experiencia"

# Creación de objetos
st.title("Sistema de Recursos Humanos - Business Corporation")

gerente = Gerente("Carlos López", "12345678")

jefes = [
    JefeArea("María Pérez", "87654321", gerente),
    JefeArea("Juan García", "56781234", gerente),
    JefeArea("Luis Torres", "34567812", gerente),
    JefeArea("Ana Mendoza", "23456789", gerente),
    JefeArea("Pedro Ruiz", "45678123", gerente)
]

for jefe in jefes:
    gerente.agregar_subordinado(jefe)

asistentes = [
    Asistente("Ana Torres", "11111111", jefes[0]),
    Asistente("Luis Mendoza", "22222222", jefes[1]),
    Asistente("Sofía Herrera", "33333333", jefes[2]),
    Asistente("Carlos Ramírez", "44444444", jefes[3]),
    Asistente("Gabriela Núñez", "55555555", jefes[4])
]

tecnicos = [
    Tecnico("José Fernández", "66666666", jefes[0], 4),
    Tecnico("Elena Ríos", "77777777", jefes[0], 2),
    Tecnico("Manuel Gómez", "88888888", jefes[1], 5),
    Tecnico("Clara Vidal", "99999999", jefes[1], 3),
    Tecnico("Ricardo Salas", "10101010", jefes[2], 1),
    Tecnico("Andrea Castro", "11111112", jefes[3], 2),
    Tecnico("Daniel Peralta", "12121212", jefes[4], 3)
]

for asistente in asistentes:
    asistente.jefe_area.agregar_subordinado(asistente)

for tecnico in tecnicos:
    tecnico.jefe_area.agregar_subordinado(tecnico)

empleados = [gerente] + jefes + asistentes + tecnicos

# Visualización en Streamlit
st.subheader("Lista de Empleados")
for empleado in empleados:
    with st.expander(empleado.get_resumen()):
        st.write(f"**Nombre:** {empleado.nombre}")
        st.write(f"**DNI:** {empleado.dni}")
        st.write(f"**Jefe inmediato:** {empleado.get_jefe_inmediato()}")
        st.write(f"**Estado:** {empleado.get_estado('Activo')}")
        
        if hasattr(empleado, 'subordinados') and empleado.subordinados:
            st.write("**Subordinados:**")
            for sub in empleado.subordinados:
                st.write(f"  - {sub.get_resumen()}")
