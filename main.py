import datetime

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = [
            "El Principito", "1984", "Cien Años de Soledad", "Don Quijote de la Mancha",
            "Hamlet", "El Hobbit", "Matar a un Ruiseñor", "Orgullo y Prejuicio",
            "La Odisea", "Fahrenheit 451"
        ]
        self.libros_prestados = {}

    def prestar_libro(self):
        nombre_libro = input("Ingrese el nombre del libro que desea prestar: ")
        if nombre_libro in self.libros_disponibles:
            fecha_vencimiento = datetime.datetime.now() + datetime.timedelta(days=7)
            self.libros_disponibles.remove(nombre_libro)
            self.libros_prestados[nombre_libro] = fecha_vencimiento
            print(f"Libro prestado con éxito. Fecha de vencimiento: {fecha_vencimiento.strftime('%Y-%m-%d')}")
        else:
            print("Libro no disponible o no encontrado.")

    def devolver_libro(self):
        nombre_libro = input("Ingrese el nombre del libro que desea devolver: ")
        if nombre_libro in self.libros_prestados:
            del self.libros_prestados[nombre_libro]
            self.libros_disponibles.append(nombre_libro)
            print("Libro devuelto con éxito.")
        else:
            print("Este libro no fue prestado por nosotros o no existe.")

    def ejecutar(self):
        while True:
            accion = input("¿Desea 'prestar' un libro o 'devolver' un libro? (escriba 'salir' para terminar): ")
            if accion.lower() == 'prestar':
                self.prestar_libro()
            elif accion.lower() == 'devolver':
                self.devolver_libro()
            elif accion.lower() == 'salir':
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el programa
biblioteca = Biblioteca()
biblioteca.ejecutar()
