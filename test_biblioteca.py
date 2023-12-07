from biblioteca import Biblioteca, Libro
import datetime

def test_buscar_libro_por_titulo():
    biblioteca = Biblioteca()
    biblioteca.libros.append(Libro("Test Libro", "Autor", 5))
    libro = biblioteca.buscar_libro_por_titulo("Test Libro")
    assert libro is not None
    assert libro.titulo == "Test Libro"

def test_es_cantidad_valida():
    libro = Libro("Libro", "Autor", 3)
    biblioteca = Biblioteca()
    assert biblioteca.es_cantidad_valida(libro, 1) is True
    assert biblioteca.es_cantidad_valida(libro, 4) is False

def test_puede_prestar():
    biblioteca = Biblioteca()
    assert biblioteca.puede_prestar(9) is True
    assert biblioteca.puede_prestar(10) is False

def test_calcular_vencimiento():
    biblioteca = Biblioteca()
    fecha_vencimiento = biblioteca.calcular_vencimiento()
    assert fecha_vencimiento == datetime.datetime.now() + datetime.timedelta(days=14)

def test_agregar_prestamo():
    biblioteca = Biblioteca()
    libro = Libro("Libro para Prueba", "Autor", 2)
    fecha_vencimiento = biblioteca.agregar_prestamo(libro, 1)
    assert len(biblioteca.prestamos) == 1
    assert libro.cantidad == 1

def test_calcular_multa():
    biblioteca = Biblioteca()
    fecha_vencimiento = datetime.datetime.now() - datetime.timedelta(days=5)
    multa = biblioteca.calcular_multa(fecha_vencimiento)
    assert multa == 5  # 5 días de retraso

# Más pruebas pueden ser añadidas para cubrir otros casos y métodos
