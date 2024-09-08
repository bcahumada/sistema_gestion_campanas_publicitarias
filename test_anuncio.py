import unittest
from anuncio import Anuncio, Video, Display, Social
from error import SubTipoInvalidoException

class TestAnuncio(unittest.TestCase):
    """Pruebas unitarias para la clase Anuncio."""

    def test_crear_anuncio(self):
        """Prueba que se pueda crear una instancia de la clase Anuncio."""
        anuncio = Anuncio()
        self.assertIsInstance(anuncio, Anuncio)

    def test_establecer_alto_ancho_validos(self):
        """Prueba que se puedan establecer valores válidos para alto y ancho."""
        anuncio = Anuncio()
        anuncio.alto = 100
        anuncio.ancho = 200
        self.assertEqual(anuncio.alto, 100)
        self.assertEqual(anuncio.ancho, 200)

    def test_establecer_alto_ancho_invalidos(self):
        """Prueba que se establezca el valor predeterminado si se ingresan valores inválidos."""
        anuncio = Anuncio()
        anuncio.alto = 0
        anuncio.ancho = -1
        self.assertEqual(anuncio.alto, 1)
        self.assertEqual(anuncio.ancho, 1)

    def test_establecer_subtipo_valido(self):
        """Prueba que se pueda establecer un subtipo válido."""
        video = Video(sub_tipo="Publicidad")
        self.assertEqual(video.sub_tipo, "Publicidad")

    def test_establecer_subtipo_invalido(self):
        """Prueba que se lance una excepción si se ingresa un subtipo inválido."""
        with self.assertRaises(SubTipoInvalidoException):
            Video(sub_tipo="Invalido")

    def test_urls(self):
        """Prueba que se puedan establecer y obtener las URLs."""
        anuncio = Anuncio()
        anuncio.url_archivo = "http://www.ejemplo.com/archivo.jpg"
        anuncio.url_clic = "http://www.ejemplo.com/destino"
        self.assertEqual(anuncio.url_archivo, "http://www.ejemplo.com/archivo.jpg")
        self.assertEqual(anuncio.url_clic, "http://www.ejemplo.com/destino")


class TestVideo(unittest.TestCase):
    """Pruebas unitarias para la clase Video."""

    def test_crear_video(self):
        """Prueba que se pueda crear una instancia de la clase Video."""
        video = Video()
        self.assertIsInstance(video, Video)

    def test_establecer_duracion_valida(self):
        """Prueba que se pueda establecer una duración válida."""
        video = Video()
        video.duracion = 30
        self.assertEqual(video.duracion, 30)

    def test_establecer_duracion_invalida(self):
        """Prueba que se establezca la duración predeterminada si se ingresa un valor inválido."""
        video = Video()
        video.duracion = -1
        self.assertEqual(video.duracion, 5)

    def test_comprimir_video(self):
        """Prueba el método comprimir_anuncio."""
        video = Video()
        with self.assertLogs() as cm:
            video.comprimir_anuncio()
        self.assertIn("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN", cm.output[0])

    def test_redimensionar_video(self):
        """Prueba el método redimensionar_anuncio."""
        video = Video()
        with self.assertLogs() as cm:
            video.redimensionar_anuncio()
        self.assertIn("RECORTE DE VIDEO NO IMPLEMENTADO AÚN", cm.output[0])


class TestDisplay(unittest.TestCase):
    """Pruebas unitarias para la clase Display."""

    def test_crear_display(self):
        """Prueba que se pueda crear una instancia de la clase Display."""
        display = Display()
        self.assertIsInstance(display, Display)

    def test_comprimir_display(self):
        """Prueba el método comprimir_anuncio."""
        display = Display()
        with self.assertLogs() as cm:
            display.comprimir_anuncio()
        self.assertIn("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN", cm.output[0])

    def test_redimensionar_display(self):
        """Prueba el método redimensionar_anuncio."""
        display = Display()
        with self.assertLogs() as cm:
            display.redimensionar_anuncio()
        self.assertIn("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN", cm.output[0])


class TestSocial(unittest.TestCase):
    """Pruebas unitarias para la clase Social."""

    def test_crear_social(self):
        """Prueba que se pueda crear una instancia de la clase Social."""
        social = Social()
        self.assertIsInstance(social, Social)

    def test_comprimir_social(self):
        """Prueba el método comprimir_anuncio."""
        social = Social()
        with self.assertLogs() as cm:
            social.comprimir_anuncio()
        self.assertIn("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN", cm.output[0])

    def test_redimensionar_social(self):
        """Prueba el método redimensionar_anuncio."""
        social = Social()
        with self.assertLogs() as cm:
            social.redimensionar_anuncio()
        self.assertIn("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN", cm.output[0])


if __name__ == "__main__":
    unittest.main()