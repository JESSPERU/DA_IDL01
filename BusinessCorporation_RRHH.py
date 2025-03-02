import streamlit as st

# Definición de clases
class Empleado:
    def __init__(self, nombre, dni, salario):
        self._nombre = nombre
        self._dni = dni
        self._salario = salario
    
    def get_nombre(self):
        return self._nombre
    
    def get_dni(self):
        return self._dni
    
    def get_salario(self):
        return self._salario
    
    def set_salario(self, nuevo_salario):
        self._salario = nuevo_salario

class Gerente(Empleado):
    def __init__(self, nombre, dni, salario):
        super().__init__(nombre, dni, salario)
        self.jefes_area = []
    
    def agregar_jefe_area(self, jefe_area):
        self.jefes_area.append(jefe_area)

class JefeArea(Empleado):
    def __init__(self, nombre, dni, salario, gerente):
        super().__init__(nombre, dni, salario)
        self.gerente = gerente
        self.asistentes = []
        self.tecnicos = []
        gerente.agregar_jefe_area(self)
    
    def agregar_asistente(self, asistente):
        self.asistentes.append(asistente)
    
    def agregar_tecnico(self, tecnico):
        self.tecnicos.append(tecnico)

class Asistente(Empleado):
    def __init__(self, nombre, dni, salario, jefe_area):
        super().__init__(nombre, dni, salario)
        self.jefe_area = jefe_area
        jefe_area.agregar_asistente(self)

class Tecnico(Empleado):
    def __init__(self, nombre, dni, salario, jefe_area):
        super().__init__(nombre, dni, salario)
        self.jefe_area = jefe_area  # Se corrige para evitar el error de atributo
        jefe_area.agregar_tecnico(self)

# Crear instancias de empleados
gerente = Gerente("Carlos Perez", "12345678", 10000)
jefe1 = JefeArea("María Lopez", "87654321", 8000, gerente)
jefe2 = JefeArea("Juan Rojas", "56781234", 7500, gerente)
asistente1 = Asistente("Pedro Díaz", "23456789", 4000, jefe1)
tecnico1 = Tecnico("Luis Torres", "34567890", 3500, jefe1)

def mostrar_empleado(empleado):
    st.subheader(f"Nombre: {empleado.get_nombre()}")
    st.write(f"DNI: {empleado.get_dni()}")
    st.write(f"Salario: {empleado.get_salario()}")

# Interfaz en Streamlit
st.title("Sistema de Recursos Humanos - Business Corporation")
st.header("Información del Personal")

empleados = [gerente, jefe1, jefe2, asistente1, tecnico1]
for empleado in empleados:
    mostrar_empleado(empleado)
