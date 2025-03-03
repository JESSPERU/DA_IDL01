import streamlit as st

# Definimos la clase padre Empleado y sus atributos comunes
class Empleado:
    def _init_(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni
        self._estado = "Activo"

    # Métodos Getter y Setter
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        self._dni = dni

    def get_resumen(self):
        return f"{self.nombre} - {self.class.name_}"

    def get_jefe_inmediato(self):
        return "No asignado"

    def get_estado(self):
        estados_validos = {"TC": "Término de contrato", "D": "Despido", "R": "Renuncia", "Activo": "Activo"}
        return estados_validos.get(self._estado, "Estado desconocido")

    def set_estado(self, nuevo_estado):
        if nuevo_estado in ["TC", "D", "R", "Activo"]:
            self._estado = nuevo_estado
        else:
            raise ValueError("Estado no válido")


class Gerente(Empleado):
    def _init_(self, nombre, dni):
        super()._init_(nombre, dni)
        self._subordinados = []

    def agregar_subordinado(self, jefe):
        if isinstance(jefe, JefeArea):
            self._subordinados.append(jefe)

    def get_subordinados(self):
        return self._subordinados


class JefeArea(Empleado):
    def _init_(self, nombre, dni, gerente):
        super()._init_(nombre, dni)
        self._gerente = gerente
        self._asistentes = []
        self._tecnicos = []

    def get_jefe_inmediato(self):
        return self._gerente.get_nombre() if self._gerente else "No tiene jefe inmediato"

    def agregar_subordinado(self, empleado):
        if isinstance(empleado, Asistente):
            if len(self._asistentes) < 2:
                self._asistentes.append(empleado)
            else:
                raise ValueError("Un jefe de área no puede tener más de 2 asistentes")
        elif isinstance(empleado, Tecnico):
            if len(self._tecnicos) < 5:
                self._tecnicos.append(empleado)
            else:
                raise ValueError("Un jefe de área no puede tener más de 5 técnicos")

    def get_subordinados(self):
        return self._asistentes + self._tecnicos


class Asistente(Empleado):
    def _init_(self, nombre, dni, jefe_area):
        super()._init_(nombre, dni)
        self._jefe_area = jefe_area

    def get_jefe_inmediato(self):
        return self._jefe_area.get_nombre() if self._jefe_area else "No tiene jefe inmediato"


class Tecnico(Empleado):
    def _init_(self, nombre, dni, jefe_area, anios_experiencia):
        super()._init_(nombre, dni)
        self._jefe_area = jefe_area
        self._anios_experiencia = anios_experiencia

    def get_jefe_inmediato(self):
        return self._jefe_area.get_nombre() if self._jefe_area else "No tiene jefe inmediato"

    def get_resumen(self):
        return f"{self.nombre} - {self.class.name_} - {self._anios_experiencia} años de experiencia"


# Creación de objetos
st.title("Sistema de Recursos Humanos - Business Corporation")

gerente = Gerente("Carlos López", "12345678")

# Jefes de las 4 áreas según la consigna
jefes = [
    JefeArea("María Pérez", "87654321", gerente),  # Marketing
    JefeArea("Juan García", "56781234", gerente),  # Sistemas
    JefeArea("Luis Torres", "34567812", gerente),  # Producción
    JefeArea("Ana Mendoza", "23456789", gerente),  # Logística
]

for jefe in jefes:
    gerente.agregar_subordinado(jefe)

# Asistentes (máximo 2 por jefe de área)
asistentes = [
    Asistente("Ana Torres", "11111111", jefes[0]),
    Asistente("Luis Mendoza", "22222222", jefes[0]),
    Asistente("Sofía Herrera", "33333333", jefes[1]),
    Asistente("Carlos Ramírez", "44444444", jefes[1]),
    Asistente("Gabriela Núñez", "55555555", jefes[2]),
    Asistente("Raúl Díaz", "66666666", jefes[2]),
    Asistente("Martha Vega", "77777777", jefes[3]),
    Asistente("Esteban Rojas", "88888888", jefes[3]),
]

# Técnicos (máximo 5 por jefe de área)
tecnicos = [
    Tecnico("José Fernández", "99999999", jefes[0], 4),
    Tecnico("Elena Ríos", "10101010", jefes[0], 2),
    Tecnico("Manuel Gómez", "11111112", jefes[1], 5),
    Tecnico("Clara Vidal", "12121212", jefes[1], 3),
    Tecnico("Ricardo Salas", "13131313", jefes[2], 1),
    Tecnico("Andrea Castro", "14141414", jefes[2], 2),
    Tecnico("Daniel Peralta", "15151515", jefes[3], 3),
    Tecnico("Carmen López", "16161616", jefes[3], 4),
]

# Asignación de subordinados
for asistente in asistentes:
    asistente._jefe_area.agregar_subordinado(asistente)

for tecnico in tecnicos:
    tecnico._jefe_area.agregar_subordinado(tecnico)

empleados = [gerente] + jefes + asistentes + tecnicos

# Visualización en Streamlit
st.subheader("Lista de Empleados")
for empleado in empleados:
    with st.expander(empleado.get_resumen()):
        st.write(f"*Nombre:* {empleado.get_nombre()}")
        st.write(f"*DNI:* {empleado.get_dni()}")
        st.write(f"*Jefe inmediato:* {empleado.get_jefe_inmediato()}")
        st.write(f"*Estado:* {empleado.get_estado()}")

        if hasattr(empleado, 'get_subordinados') and empleado.get_subordinados():
            st.write("*Subordinados:*")
            for sub in empleado.get_subordinados():
                st.write(f"  - {sub.get_resumen()}")