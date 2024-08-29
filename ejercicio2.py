#importa herramientas de fecha 
from datetime import datetime

# Clase que representa un libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo  # Título del libro
        self.autor = autor  # Autor del libro

# Clase que representa un usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del usuario

# Clase que maneja el préstamo de un libro, usuario al que se presto, fecha de prestamo, fecha limite, 
#estado del libro y un contador de los dias de retraso
class Prestamo:
    def __init__(self, libro, usuario, fecha_devolucion):
        self.libro = libro  
        self.usuario = usuario  
        self.fecha_prestamo = datetime.now()  
        self.fecha_devolucion = fecha_devolucion  
        self.devuelto = False  
        self.retrasos = 0  

    # Método para devolver el libro, fecha actual de la devolucion, marca el libro como devuelto, 
    #incrementa el contador de retrasos
    def devolver_libro(self):
        fecha_actual = datetime.now()  
        self.devuelto = True  
        if fecha_actual > self.fecha_devolucion:
            dias_tarde = (fecha_actual - self.fecha_devolucion).days  
            self.retrasos += 1  
            if self.retrasos == 1:
                print(f"El libro '{self.libro.titulo}' ha sido devuelto tarde. Días de retraso: {dias_tarde}.")
                print("Aviso: Si vuelve a devolver el libro tarde, se aplicará una sanción monetaria.")
            else:
                print(f"El libro '{self.libro.titulo}' ha sido devuelto tarde nuevamente. Se aplicará una sanción monetaria.")
        else:
            print(f"El libro '{self.libro.titulo}' ha sido devuelto a tiempo.")

# Clase que maneja la biblioteca y lista para almacenar los prestamos
class Biblioteca:
    def __init__(self):
        self.prestamos = []  

    # Método para realizar un nuevo préstamo, convierte texto a fecha, crea un nuevo prestamo y añade el prestamo
    def realizar_prestamo(self, libro, usuario):
        fecha_devolucion_str = input(f"Ingrese la fecha de devolución para el libro '{libro.titulo}' (formato AAAA-MM-DD): ")
        fecha_devolucion = datetime.strptime(fecha_devolucion_str, "%Y-%m-%d")  
        nuevo_prestamo = Prestamo(libro, usuario, fecha_devolucion)  
        self.prestamos.append(nuevo_prestamo)  
        print(f"Préstamo realizado. El libro '{libro.titulo}' debe ser devuelto antes del {fecha_devolucion}.")
    
    # Método para devolver un libro y procesar la devolucion del libro
    def devolver_libro(self, libro, usuario):
        for prestamo in self.prestamos:
            if prestamo.libro == libro and prestamo.usuario == usuario and not prestamo.devuelto:
                prestamo.devolver_libro()  
                return
        print(f"No se encontró un préstamo activo para el libro '{libro.titulo}'.")



# Crear una instancia de la biblioteca
biblioteca = Biblioteca()

# Pedir al usuario que ingrese libros
num_libros = int(input("¿Cuántos libros desea agregar? "))
libros = []
for _ in range(num_libros):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    libros.append(Libro(titulo, autor))  # Añade el libro a la lista

# Pedir al usuario que ingrese usuarios
num_usuarios = int(input("¿Cuántos usuarios desea agregar? "))
usuarios = []
for _ in range(num_usuarios):
    nombre = input("Ingrese el nombre del usuario: ")
    usuarios.append(Usuario(nombre))  # Añade el usuario a la lista

# Menú para realizar acciones en la biblioteca
continuar = True
while continuar:
    print("\nOpciones:")
    print("1. Realizar préstamo")
    print("2. Devolver libro")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Realizar un préstamo
        print("\nLibros disponibles:")
        for i, libro in enumerate(libros):
            print(f"{i + 1}. {libro.titulo} por {libro.autor}")
        libro_idx = int(input("Seleccione el número del libro a prestar: ")) - 1
        
        print("\nUsuarios disponibles:")
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. {usuario.nombre}")
        usuario_idx = int(input("Seleccione el número del usuario: ")) - 1

        biblioteca.realizar_prestamo(libros[libro_idx], usuarios[usuario_idx])

    elif opcion == "2":
        # Devolver un libro
        print("\nLibros prestados:")
        for i, prestamo in enumerate(biblioteca.prestamos):
            if not prestamo.devuelto:
                print(f"{i + 1}. {prestamo.libro.titulo} por {prestamo.libro.autor} (Prestado a {prestamo.usuario.nombre})")
        prestamo_idx = int(input("Seleccione el número del libro a devolver: ")) - 1

        biblioteca.devolver_libro(biblioteca.prestamos[prestamo_idx].libro, biblioteca.prestamos[prestamo_idx].usuario)

    elif opcion == "3":
        # Salir del programa
        print("Saliendo del sistema...")
        continuar = False

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
