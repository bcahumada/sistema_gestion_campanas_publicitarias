class LargoExcedidoException(Exception):
    """Excepción lanzada cuando se excede la longitud máxima permitida."""

    def __init__(self, mensaje="Se ha excedido la longitud máxima permitida."):
        super().__init__(mensaje)

class SubTipoInvalidoException(Exception):
    """Excepción lanzada cuando se proporciona un subtipo de anuncio no válido."""

    def __init__(self, mensaje="El subtipo ingresado no es válido."):
        super().__init__(mensaje)