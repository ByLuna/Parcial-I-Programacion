
# Importa herramientas para manejar fechas y tiempos
from datetime import datetime, timedelta

#almacena el nombre, el motivo de la consulta y inicia la fecha de la consulta del paciente.
class paciente:
    def __init__(self, nombre, motivo_conslt):
        self.nombre = nombre
        self.motivo_conslt = motivo_conslt
        self.fechaConslt = None

#asigna la fecha de la consulta e informa al paciente.
    def asigConslt(self, fecha):
            self.fechaConslt = fecha
            print(f"consulta asignada a {self.nombre} el {self.fechaConslt}")
    
#clase que almacena el nombre del doctor
class doctor:
     def __init__(self, nombre):
          self.nombre = nombre

#clase secretaria y en esta tambien la lista que almacena los pacientes registrados.
class secretaria:
     def __init__(self):
          self.pacientes = []

     def registrPaciente(self, nombre,motivo_conslt):
          pacienteExist = self.buscPaciente(nombre) #verifica si el paciente esta registrado
          if pacienteExist:
               #si el paciente ya tiene una consulta lo pasara a la sala de espera.
               print(f"{nombre} ya tiene una consulta programada. se le pasara a sala de espera.")
          else:
            nuevo_paciente = paciente(nombre, motivo_consulta)
            self.pacientes.append(nuevo_paciente)
            fecha_consulta = datetime.now() + timedelta(days=1)
            nuevo_paciente.asigConslt(fecha_consulta)
    #busca en la lista de pacientes si este ya existe y lo retorna si lo encuentra
     def buscPaciente(self, nombre):
        for paciente in self.pacientes:
            if paciente.nombre == nombre:
                return paciente
        return None
#clase consultorio en esta almacena la lista de doctores y se encuentra la instancia de la secretaria.
class Consultorio:
    def __init__(self):
        self.doctores = []
        self.secretaria = secretaria()
#crea un nuevo doctor y se añade a la lista
    def agregar_doctor(self, nombre):
        nuevo_doctor = doctor(nombre)
        self.doctores.append(nuevo_doctor)

    # Solicita a la secretaria que registre al paciente.
    def atender_paciente(self, nombre, motivo_consulta):
        self.secretaria.registrPaciente(nombre, motivo_consulta)

# Crear una instancia del consultorio
consultorio = Consultorio()

# Agregar doctores al consultorio
num_doctores = int(input("¿Cuántos doctores desea agregar al consultorio? "))
for _ in range(num_doctores):
    nombre_doctor = input("Ingrese el nombre del doctor: ")
    consultorio.agregar_doctor(nombre_doctor)

# Bucle principal para registrar pacientes o salir
while True:
    print("\nOpciones:")
    print("1. Registrar nuevo paciente")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Si elige registrar un paciente, pide nombre y motivo de consulta
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        motivo_consulta = input("Ingrese el motivo de la consulta: ")
        consultorio.atender_paciente(nombre_paciente, motivo_consulta)
        # Si elige salir, se termina el programa
    elif opcion == "2":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")