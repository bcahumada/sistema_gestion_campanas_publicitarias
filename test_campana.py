import unittest
from campana import Campana
from error import LargoExcedidoException
from datetime import date

class TestCampana(unittest.TestCase):
    """Pruebas unitarias para la clase Campana."""


    def test_crear_campana_nombre_valido(self):
        """Prueba que se pueda crear una campaña con un nombre válido."""
        nombre = "Campaña de prueba"
        campana = Campana(nombre)
        self.assertEqual(campana.nombre, nombre)


    def test_crear_campana_nombre_excede_longitud(self):
        """Prueba que se lance una excepción si el nombre excede la longitud máxima."""
        nombre = "a" * 251  # Nombre con más de 250 caracteres
        with self.assertRaises(LargoExcedidoException):
            Campana(nombre)


    def test_modificar_nombre_valido(self):
        """Prueba que se pueda modificar el nombre de la campaña con un nombre válido."""
        campana = Campana("Nombre original")
        nuevo_nombre = "Nuevo nombre"
        campana.nombre = nuevo_nombre
        self.assertEqual(campana.nombre, nuevo_nombre)


    def test_modificar_nombre_excede_longitud(self):
        """Prueba que se lance una excepción si el nuevo nombre excede la longitud máxima."""
        campana = Campana("Nombre original")
        nuevo_nombre = "a" * 251
        with self.assertRaises(LargoExcedidoException):
            campana.nombre = nuevo_nombre


    def test_agregar_anuncio(self):
        """Prueba que se pueda agregar un anuncio a la campaña."""
        campana = Campana("Campaña de prueba")
        anuncio = Anuncio()  # posible usar una instancia de una subclase de Anuncio
        campana.anuncios.append(anuncio)
        self.assertIn(anuncio, campana.anuncios)


    def test_fecha_inicio_termino(self):
        """Prueba que se puedan establecer y obtener las fechas de inicio y término."""
        fecha_inicio = date(2024, 1, 1)
        fecha_termino = date(2024, 12, 31)
        campana = Campana("Campaña de prueba", fecha_inicio=fecha_inicio, fecha_termino=fecha_termino)
        self.assertEqual(campana.fecha_inicio, fecha_inicio)
        self.assertEqual(campana.fecha_termino, fecha_termino)


    def test_fecha_inicio_mayor_que_fecha_termino(self):
        """Prueba que se lance una excepción si la fecha de inicio es mayor que la fecha de término."""
        fecha_inicio = date(2024, 12, 31)
        fecha_termino = date(2024, 1, 1)
        with self.assertRaises(ValueError) as context:
            Campana("Campaña de prueba", fecha_inicio=fecha_inicio, fecha_termino=fecha_termino)
        self.assertEqual(str(context.exception), "La fecha de inicio no puede ser posterior a la fecha de término.")


    def test_campana_con_multiples_anuncios(self):
        """Prueba la creación y modificación de una campaña con varios anuncios."""
        campana = Campana("Campaña con varios anuncios")
        video = Video(sub_tipo="Publicidad", url_archivo="http://video.com", url_clic="http://video.com/clic", duracion=15)
        display = Display(sub_tipo="Banner", url_archivo="http://banner.com", url_clic="http://banner.com/clic")
        campana.anuncios.extend([video, display])

        self.assertEqual(len(campana.anuncios), 2)
        self.assertIn(video, campana.anuncios)
        self.assertIn(display, campana.anuncios)

        # Modificar un anuncio
        campana.anuncios[0].duracion = 20
        self.assertEqual(campana.anuncios[0].duracion, 20)

if __name__ == "__main__":
    unittest.main()