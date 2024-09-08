from abc import ABC, abstractmethod
from error import SubTipoInvalidoException

class Anuncio(ABC):
    """
    Clase base abstracta que representa un anuncio genérico.
    """

    SUB_TIPOS = {}

    def __init__(self, sub_tipo=None, url_archivo=None, url_clic=None):
        """
        Inicializa una instancia de la clase Anuncio.

        Args:
            sub_tipo (str, optional): Subtipo del anuncio. Por defecto es None.
            url_archivo (str, optional): URL del archivo del anuncio. Por defecto es None.
            url_clic (str, optional): URL de destino del clic en el anuncio. Por defecto es None.
        """
        self._alto = 1
        self._ancho = 1
        self._sub_tipo = sub_tipo
        self._url_archivo = url_archivo
        self._url_clic = url_clic

    def __init_subclass__(cls, **kwargs):
        """
        Registra los SUB_TIPOS de la subclase en el diccionario de la clase Anuncio.
        """
        super().__init_subclass__(**kwargs)
        Anuncio.SUB_TIPOS[cls.__name__] = cls.SUB_TIPOS

    @property
    def alto(self):
        """int: Regresa la altura del anuncio."""
        return self._alto

    @alto.setter
    def alto(self, valor):
        """
        Establece la altura del anuncio.

        Args:
            valor (int): Nueva altura del anuncio. Si es menor o igual a 0, se establece en 1.
        """
        self._alto = valor if valor > 0 else 1

    @property
    def ancho(self):
        """int: Regresa el ancho del anuncio."""
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        """
        Establece el ancho del anuncio.

        Args:
            valor (int): Nuevo ancho del anuncio. Si es menor o igual a 0, se establece en 1.
        """
        self._ancho = valor if valor > 0 else 1

    @property
    def sub_tipo(self):
        """str: Regresa el subtipo del anuncio."""
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor):
        """
        Establece el subtipo del anuncio.

        Args:
            valor (str): Nuevo subtipo del anuncio.

        Raises:
            SubTipoInvalidoException: Si el subtipo no está permitido para el tipo de anuncio.
        """
        if valor in self.SUB_TIPOS.get(type(self).__name__, []):
            self._sub_tipo = valor
        else:
            raise SubTipoInvalidoException(
                f"Subtipo '{valor}' no válido para {type(self).__name__}."
            )

    @property
    def url_archivo(self):
        """str: Regresa la URL del archivo del anuncio."""
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, nueva_url):
        """Establece la URL del archivo del anuncio."""
        self._url_archivo = nueva_url

    @property
    def url_clic(self):
        """str: Regresa la URL de destino del clic en el anuncio."""
        return self._url_clic

    @url_clic.setter
    def url_clic(self, nueva_url):
        """Establece la URL de destino del clic en el anuncio."""
        self._url_clic = nueva_url

    @staticmethod
    def mostrar_formatos(tipo_anuncio=None):
        """Devuelve un string con los formatos de anuncios y subtipos disponibles."""
        formatos_str = "Subtipos:\n"
        if tipo_anuncio:
            subtipos = Anuncio.SUB_TIPOS.get(tipo_anuncio)
            if subtipos:
                formatos_str += f"De {tipo_anuncio}: "
                # Iteramos sobre los valores del diccionario subtipos
                for i, subtipo in enumerate(subtipos[tipo_anuncio]):
                    formatos_str += f"'{subtipo}'"
                    if i < len(subtipos[tipo_anuncio]) - 1:
                        formatos_str += " y "
                    else:
                        formatos_str += "\n"
        else:
            for formato, subtipos in Anuncio.SUB_TIPOS.items():
                formatos_str += f"De {formato}: "
                # Iteramos sobre los valores del diccionario subtipos
                for i, subtipo in enumerate(subtipos[formato]):
                    formatos_str += f"'{subtipo}'"
                    if i < len(subtipos[formato]) - 1:
                        formatos_str += " y "
                    else:
                        formatos_str += "\n"
        return formatos_str

    @abstractmethod
    def comprimir_anuncio(self):
        """Comprime el anuncio."""
        print(f"La compresión de {self.__class__.__name__} no está implementada aún.")

    @abstractmethod
    def redimensionar_anuncio(self):
        """Redimensiona el anuncio."""
        print(f"El redimensionamiento de {self.__class__.__name__} no está implementado aún.")


class Video(Anuncio):
    """
    Clase que representa un anuncio de video.
    """

    SUB_TIPOS = {"Video": ("Publicidad", "Tutorial")}

    def __init__(self, sub_tipo=None, url_archivo=None, url_clic=None, duracion=5):
        """
        Inicializa una instancia de la clase Video.

        Args:
            sub_tipo (str, optional): Subtipo del anuncio de video. Por defecto es None.
            url_archivo (str, optional): URL del archivo del anuncio. Por defecto es None.
            url_clic (str, optional): URL de destino del clic en el anuncio. Por defecto es None.
            duracion (int, optional): Duración del video en segundos. Por defecto es 5.
        """
        super().__init__(sub_tipo, url_archivo, url_clic)
        self._duracion = duracion

    @property
    def duracion(self):
        """int: Regresa la duración del video."""
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        """
        Establece la duración del video.

        Args:
            valor (int): Nueva duración del video en segundos. Si es menor o igual a 0, se establece en 5.
        """
        self._duracion = valor if valor > 0 else 5

    def comprimir_anuncio(self):
        """Comprime el anuncio de video (no implementado)."""
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Redimensiona el anuncio de video (no implementado)."""
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    """Clase que representa un anuncio display."""

    SUB_TIPOS = {"Display": ("Banner", "Sidebar")}

    def comprimir_anuncio(self):
        """Comprime el anuncio display (no implementado)."""
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Redimensiona el anuncio display (no implementado)."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")


class Social(Anuncio):
    """Clase que representa un anuncio de redes sociales."""

    SUB_TIPOS = {"Social": ("Post", "Story")}

    def comprimir_anuncio(self):
        """Comprime el anuncio de redes sociales (no implementado)."""
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Redimensiona el anuncio de redes sociales (no implementado)."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")