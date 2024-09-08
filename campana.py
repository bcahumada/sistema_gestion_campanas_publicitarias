from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoException
from datetime import date

class Campana:
    """
    Representa una campaña publicitaria con un nombre, lista de anuncios y fechas.

    Atributos:
        _nombre (str): Nombre de la campaña (máximo 250 caracteres).
        _anuncios (list): Lista de objetos Anuncio que pertenecen a la campaña.
        _fecha_inicio (date): Fecha de inicio de la campaña.
        _fecha_termino (date): Fecha de término de la campaña.
    """

    def __init__(self, nombre, anuncios=None, fecha_inicio=None, fecha_termino=None):
        """
        Inicializa una instancia de la clase Campana.

        Args:
            nombre (str): Nombre de la campaña.
            anuncios (list, optional): Lista de anuncios. Por defecto es None.
            fecha_inicio (date, optional): Fecha de inicio. Por defecto es None.
            fecha_termino (date, optional): Fecha de término. Por defecto es None.

        Raises:
            LargoExcedidoException: Si el nombre de la campaña excede los 250 caracteres.
        """
        if len(nombre) > 250:
            raise LargoExcedidoException("El nombre de la campaña excede los 250 caracteres.")
        self._nombre = nombre
        self._anuncios = anuncios if anuncios is not None else []
        self._fecha_inicio = fecha_inicio
        self._fecha_termino = fecha_termino

    @property
    def nombre(self):
        """str: Regresa el nombre de la campaña."""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """
        Establece un nuevo nombre para la campaña.

        Args:
            nuevo_nombre (str): El nuevo nombre de la campaña.

        Raises:
            LargoExcedidoException: Si el nuevo nombre excede los 250 caracteres.
        """
        if len(nuevo_nombre) > 250:
            raise LargoExcedidoException("El nombre de la campaña excede los 250 caracteres.")
        self._nombre = nuevo_nombre

    @property
    def anuncios(self):
        """list: Regresa la lista de anuncios de la campaña."""
        return self._anuncios
    
    @property
    def fecha_inicio(self):
        """date: Retorna la fecha de inicio de la campaña."""
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        """Establece una nueva fecha de inicio para la campaña."""
        self._fecha_inicio = nueva_fecha_inicio

    @property
    def fecha_termino(self):
        """date: Retorna la fecha de término de la campaña."""
        return self._fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, nueva_fecha_termino):
        """Establece una nueva fecha de término para la campaña."""
        self._fecha_termino = nueva_fecha_termino

    def __str__(self):
        """
        Retorna una representación legible de la Campaña.

        Returns:
            str: Resumen de la campaña con su nombre y cantidad de anuncios por tipo.
        """
        resumen = f"Nombre de la campaña: {self._nombre}\n"
        if self._fecha_inicio:
            resumen += f"Fecha de inicio: {self._fecha_inicio.strftime('%Y-%m-%d')}\n"
        if self._fecha_termino:
            resumen += f"Fecha de término: {self._fecha_termino.strftime('%Y-%m-%d')}\n"

        resumen += "Anuncios:\n"
        conteos = {'Video': 0, 'Display': 0, 'Social': 0}
        for anuncio in self._anuncios:
            conteos[type(anuncio).__name__] += 1
        for tipo, cantidad in conteos.items():
            resumen += f"- {cantidad} {tipo}\n"
        return resumen