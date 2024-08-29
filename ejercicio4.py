# Creamos nuestra clase Animal donde definimos el nombre, especie, edad, area donde se encuentra y si se encuentra en tratamiento o no
class Animal:
    def __init__(self, nombre, especie, edad, area, en_tratamiento=False, tratamiento=None):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.area = area
        self.en_tratamiento = en_tratamiento
        self.tratamiento = tratamiento
#Utilizamos detalles para verificar si esta en tratamiento o no
    def detalles(self):
        tratamiento_info = str(self.tratamiento) if self.en_tratamiento else 'No'
        return [self.nombre, self.especie, self.edad, self.area, tratamiento_info]

#Esta clase reprenta las Areas en el zoológico donde reside cada animal, ya sea en las zonas de selva, el la desiertica o en acuario
class Area:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"Área: {self.nombre} - {self.descripcion}"


# Aqui definimos que tipo de tratamiento necesita cada animal dentro del zoologico 
class Tratamiento:
    def __init__(self, nombre, dosis, frecuencia):
        self.nombre = nombre
        self.dosis = dosis
        self.frecuencia = frecuencia

    def __str__(self):
        return f"{self.nombre}, Dosis: {self.dosis}, Frecuencia: {self.frecuencia}"


# Usamos esta clase para poder llevar un registro si en algun momento los animales son atendidos por otras personas aparte del encargado
class Veterinario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def generar_reporte(self):
        headers = ["Nombre", "Especie", "Edad", "Área", "Tratamiento"]
        row_format = "{:<15} {:<20} {:<5} {:<15} {:<25}"
        
        print(row_format.format(*headers))
        print("-" * 80)
        
        for animal in self.animales:
            detalles = animal.detalles()
            print(row_format.format(*detalles))

# Ejemplos de áreas en el zoológico
area_a = Area("Selva", "Zona con fauna tropical")
area_b = Area("Desierto", "Área con animales del desierto")
area_c = Area("Acuático", "Zona con fauna marina")

# Ejemplos de tratamientos
tratamiento_a = Tratamiento("Desparasitante", "5ml", "Cada 3 meses")
tratamiento_b = Tratamiento("Antibiótico", "10ml", "Cada 12 horas")

# Creación de un veterinario
veterinario = Veterinario("Dr. López")

# Agregando animales
animal1 = Animal("Tigre", "Panthera tigris", 5, area_a.nombre, en_tratamiento=True, tratamiento=tratamiento_a)
animal2 = Animal("Elefante", "Loxodonta africana", 10, area_a.nombre, en_tratamiento=False)
animal3 = Animal("Cangrejo", "U. mjoe", 2, area_c.nombre, en_tratamiento=True, tratamiento=tratamiento_b)
animal4 = Animal("Cebra", "Equus zebra", 4, area_b.nombre, en_tratamiento=False)
animal5 = Animal("Foca", "Phoca vitulina", 6, area_c.nombre, en_tratamiento=True, tratamiento=tratamiento_a)
animal6 = Animal("León", "Panthera leo", 8, area_a.nombre, en_tratamiento=False)
animal7 = Animal("Camello", "Camelus dromedarius", 5, area_b.nombre, en_tratamiento=True, tratamiento=tratamiento_b)
animal8 = Animal("Pingüino", "Spheniscidae", 3, area_c.nombre, en_tratamiento=False)

# Agregando animales al veterinario
veterinario.agregar_animal(animal1)
veterinario.agregar_animal(animal2)
veterinario.agregar_animal(animal3)
veterinario.agregar_animal(animal4)
veterinario.agregar_animal(animal5)
veterinario.agregar_animal(animal6)
veterinario.agregar_animal(animal7)
veterinario.agregar_animal(animal8)

# Generando el reporte de animales
veterinario.generar_reporte()
