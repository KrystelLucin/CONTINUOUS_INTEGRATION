import datetime

class Libro:
    def __init__(self, titulo, autor, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad

class Prestamo:
    def __init__(self, libro, cantidad, fecha_vencimiento):
        self.libro = libro
        self.cantidad = cantidad
        self.fecha_vencimiento = fecha_vencimiento

class Biblioteca:
    def __init__(self):
        self.libros = [
            Libro("El Principito", "Antoine de Saint-Exupéry", 3),
            Libro("1984", "George Orwell", 5),
            Libro("Cien Años de Soledad", "Gabriel García Márquez", 4),
            Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 2),
            Libro("Hamlet", "William Shakespeare", 6),
            Libro("El Hobbit", "J.R.R. Tolkien", 3),
            Libro("Matar a un Ruiseñor", "Harper Lee", 4),
            Libro("Orgullo y Prejuicio", "Jane Austen", 5),
            Libro("La Odisea", "Homero", 2),
            Libro("Fahrenheit 451", "Ray Bradbury", 3)
        ]
        self.prestamos = []

    def mostrar_libros(self):
        for libro in self.libros:
            print(f"{libro.titulo} - {libro.autor}, Cantidad disponible: {libro.cantidad}")

    def buscar_libro_por_titulo(self, titulo):
        return next((libro for libro in self.libros if libro.titulo == titulo), None)

    def es_cantidad_valida(self, libro, cantidad):
        return 0 < cantidad <= libro.cantidad

    def puede_prestar(self, cantidad_actual):
        return cantidad_actual < 10

    def calcular_vencimiento(self, dias=14):
        return datetime.datetime.now() + datetime.timedelta(days=dias)

    def agregar_prestamo(self, libro, cantidad):
        fecha_vencimiento = self.calcular_vencimiento()
        self.prestamos.append(Prestamo(libro, cantidad, fecha_vencimiento))
        libro.cantidad -= cantidad
        return fecha_vencimiento

    def calcular_multa(self, fecha_vencimiento, tarifa_por_dia=1):
        dias_retraso = (datetime.datetime.now() - fecha_vencimiento).days
        return max(0, dias_retraso) * tarifa_por_dia

    def procesar_prestamo(self):
        self.mostrar_libros()
        libros_seleccionados = []
        total_libros_seleccionados = 0

        while total_libros_seleccionados < 10:
            titulo = input("Ingrese el título del libro (o 'salir' para finalizar): ")
            if titulo.lower() == 'salir':
                break

            libro = self.buscar_libro_por_titulo(titulo)
            if libro is None:
                print("Libro no encontrado.")
                continue

            cantidad = int(input("Ingrese la cantidad: "))
            if not self.es_cantidad_valida(libro, cantidad):
                print("Cantidad no válida.")
                continue

            total_libros_seleccionados += cantidad
            libros_seleccionados.append((libro, cantidad))

        for libro, cantidad in libros_seleccionados:
            fecha_vencimiento = self.agregar_prestamo(libro, cantidad)
            print(f"Prestaste {cantidad} copia(s) de '{libro.titulo}'. Fecha de vencimiento: {fecha_vencimiento.strftime('%Y-%m-%d')}")

    def devolver_libro(self):
        titulo = input("Ingrese el título del libro que desea devolver: ")
        prestamo = next((p for p in self.prestamos if p.libro.titulo == titulo), None)
        if prestamo is None:
            print("Este libro no fue prestado o no existe.")
            return

        multa = self.calcular_multa(prestamo.fecha_vencimiento)
        print(f"Libro '{titulo}' devuelto. Multa por retraso: ${multa}")

        prestamo.libro.cantidad += prestamo.cantidad
        self.prestamos.remove(prestamo)

    def ejecutar(self):
        while True:
            accion = input("¿Desea 'prestar' un libro, 'devolver' un libro, o 'salir'? ")
            if accion.lower() == 'prestar':
                self.procesar_prestamo()
            elif accion.lower() == 'devolver':
                self.devolver_libro()
            elif accion.lower() == 'salir':
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

# Si este archivo se ejecuta directamente, inicia la aplicación
if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.ejecutar()
