from campana import Campana
from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoException, SubTipoInvalidoException
from datetime import date
import re  

def validar_fecha(fecha_str):
    """Valida que la fecha tenga el formato YYYY-MM-DD."""
    try:
        date.fromisoformat(fecha_str)
        return True
    except ValueError:
        return False

def validar_url(url):
    """Valida que la URL tenga un formato válido usando una expresión regular."""
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// o https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # Dominio
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...o dirección IP
        r'(?::\d+)?'  # puerto opcional
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def crear_campana(campanas):
    """Crea una nueva campaña y la agrega a la lista de campañas."""
    nombre = input("¿Cómo quieres llamar a tu campaña?: ")
    while True:
        fecha_inicio_str = input("Ingresa la fecha de inicio (YYYY-MM-DD, opcional): ")
        if not fecha_inicio_str:
            fecha_inicio = None
            break
        elif validar_fecha(fecha_inicio_str):
            fecha_inicio = date.fromisoformat(fecha_inicio_str)
            break
        else:
            print("Ups! El formato de la fecha no es correcto. Usa YYYY-MM-DD. Ejemplo: 2024-02-09")

    while True:
        fecha_termino_str = input("Ingresa la fecha de término (YYYY-MM-DD, opcional): ")
        if not fecha_termino_str:
            fecha_termino = None
            break
        elif validar_fecha(fecha_termino_str):
            fecha_termino = date.fromisoformat(fecha_termino_str)
            break
        else:
            print("Ups! El formato de la fecha no es correcto. Usa YYYY-MM-DD. Ejemplo: 2024-02-09")

    try:
        campana = Campana(nombre, fecha_inicio=fecha_inicio, fecha_termino=fecha_termino)
        campanas.append(campana)
        print("¡Campaña creada con éxito!")
    except LargoExcedidoException as e:
        print(f"Error al crear la campaña: {e}")

def mostrar_campanas(campanas):
    """Muestra la información de todas las campañas."""
    if not campanas:
        print("Aún no has creado ninguna campaña.")
        return

    print("\n--- Campañas existentes ---")
    for i, campana in enumerate(campanas):
        print(f"{i+1}. {campana.nombre}")

def mostrar_campana(campana):
    """Muestra la información de una campaña específica."""
    if campana:
        print(campana)
    else:
        print("No se ha seleccionado ninguna campaña.")

def modificar_campana(campanas):
    """Modifica una campaña existente."""
    if not campanas:
        print("Aún no has creado ninguna campaña.")
        return

    mostrar_campanas(campanas)

    while True:
        try:
            opcion = int(input("Selecciona el número de la campaña a modificar: "))
            if 1 <= opcion <= len(campanas):
                campana = campanas[opcion - 1]
                break
            else:
                print("Opción inválida. Intenta de nuevo.")
        except ValueError:
            print("Ingresa un número válido.")

    while True:
        print("\n--- Modificar Campaña ---")
        print("a. Cambiar nombre")
        print("b. Agregar anuncio")
        print("c. Modificar anuncio")
        print("d. Volver al menú principal")

        opcion = input("Elige una opción: ").lower()

        if opcion == 'a':
            nuevo_nombre = input("Ingresa el nuevo nombre de la campaña: ")
            try:
                campana.nombre = nuevo_nombre
                print("Nombre de la campaña actualizado correctamente.")
            except LargoExcedidoException as e:
                print(f"Error: {e}")
        elif opcion == 'b':
            campana = agregar_anuncio(campana)
        elif opcion == 'c':
            campana = modificar_anuncio(campana)
        elif opcion == 'd':
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
    return campana

def agregar_anuncio(campana):
    """Agrega un nuevo anuncio a la campaña."""
    print("\n--- Agregar Anuncio ---")
    print("a. Video")
    print("b. Display")
    print("c. Social")

    while True:
        tipo_anuncio = input("Elige el tipo de anuncio: ").lower()
        if tipo_anuncio in ("a", "b", "c"):
            break
        print("Opción inválida. Intenta de nuevo.")

    # Obtener el nombre de la clase del tipo de anuncio
    tipo_anuncio_nombre = {"a": "Video", "b": "Display", "c": "Social"}[tipo_anuncio]

    subtipos_str = Anuncio.mostrar_formatos(tipo_anuncio_nombre)
    while True:
        sub_tipo = input(f"Elige el subtipo del anuncio:\n{subtipos_str}Subtipo: ")
        if sub_tipo:  # Verificar si el subtipo no está vacío
            break
        print("Error: Debes elegir un subtipo.")

    while True:
        url_archivo = input("Ingresa la URL del archivo del anuncio: ")
        if validar_url(url_archivo):
            break
        else:
            print("URL inválida. Intenta de nuevo.")

    while True:
        url_clic = input("Ingresa la URL de destino del clic: ")
        if validar_url(url_clic):
            break
        else:
            print("URL inválida. Intenta de nuevo.")

    try:
        if tipo_anuncio == "a":
            if sub_tipo in Video.SUB_TIPOS["Video"]:
                while True:
                    try:
                        duracion = int(input("Ingresa la duración del video (segundos): "))
                        break
                    except ValueError:
                        print("Duración inválida. Ingresa un número entero.")
                anuncio = Video(sub_tipo, url_archivo, url_clic, duracion)
                campana.anuncios.append(anuncio)
            else:
                print(f"Error: Subtipo '{sub_tipo}' no es válido para Video.")
        elif tipo_anuncio == "b":
            if sub_tipo in Display.SUB_TIPOS["Display"]:
                anuncio = Display(sub_tipo, url_archivo, url_clic)
                campana.anuncios.append(anuncio)
            else:
                print(f"Error: Subtipo '{sub_tipo}' no es válido para Display.")
        else:
            if sub_tipo in Social.SUB_TIPOS["Social"]:
                anuncio = Social(sub_tipo, url_archivo, url_clic)
                campana.anuncios.append(anuncio)
            else:
                print(f"Error: Subtipo '{sub_tipo}' no es válido para Social.")

        print("¡Anuncio agregado correctamente!")
    except SubTipoInvalidoException as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Ingresa una duración válida (un número entero).")

    return campana

def modificar_anuncio(campana):
    """Modifica un anuncio existente en la campaña."""
    if not campana.anuncios:
        print("No hay anuncios en esta campaña todavía.")
        return campana

    print("\n--- Modificar Anuncio ---")
    for i, anuncio in enumerate(campana.anuncios):
        print(f"{i+1}. {anuncio.__class__.__name__} (Subtipo: {anuncio.sub_tipo})")

    while True:
        try:
            opcion = int(input("Selecciona el número del anuncio a modificar: "))
            if 1 <= opcion <= len(campana.anuncios):
                anuncio_a_modificar = campana.anuncios[opcion - 1]
                break
            else:
                print("Opción inválida. Intenta de nuevo.")
        except ValueError:
            print("Ingresa un número válido.")

    while True:
        # Mostrar opciones de modificación según el tipo de anuncio
        if isinstance(anuncio_a_modificar, Video):
            print("\n--- Modificar Anuncio de Video ---")
            print("a. Cambiar subtipo")
            print("b. Cambiar URL del archivo")
            print("c. Cambiar URL de destino del clic")
            print("d. Cambiar duración")
            print("e. Volver al menú anterior")
        elif isinstance(anuncio_a_modificar, Display):
            print("\n--- Modificar Anuncio Display ---")
            print("a. Cambiar subtipo")
            print("b. Cambiar URL del archivo")
            print("c. Cambiar URL de destino del clic")
            print("d. Volver al menú anterior")
        elif isinstance(anuncio_a_modificar, Social):
            print("\n--- Modificar Anuncio Social ---")
            print("a. Cambiar subtipo")
            print("b. Cambiar URL del archivo")
            print("c. Cambiar URL de destino del clic")
            print("d. Volver al menú anterior")

        opcion_modificar = input("Elige una opción: ").lower()

        try:
            if opcion_modificar == "a":
                # Obtener el string formateado de subtipos
                tipo_anuncio = type(anuncio_a_modificar).__name__
                subtipos_str = Anuncio.mostrar_formatos(tipo_anuncio)
                nuevo_subtipo = input(
                    f"Ingresa el nuevo subtipo del anuncio:\n{subtipos_str}Subtipo: "
                )
                anuncio_a_modificar.sub_tipo = nuevo_subtipo
                print("Subtipo del anuncio actualizado correctamente.")
            elif opcion_modificar == "b":
                while True:
                    nueva_url_archivo = input(
                        "Ingresa la nueva URL del archivo del anuncio: "
                    )
                    if validar_url(nueva_url_archivo):
                        anuncio_a_modificar.url_archivo = nueva_url_archivo
                        print("URL del archivo del anuncio actualizada correctamente.")
                        break
                    else:
                        print("URL inválida. Intenta de nuevo.")
            elif opcion_modificar == "c":
                while True:
                    nueva_url_clic = input(
                        "Ingresa la nueva URL de destino del clic: "
                    )
                    if validar_url(nueva_url_clic):
                        anuncio_a_modificar.url_clic = nueva_url_clic
                        print("URL de destino del clic actualizada correctamente.")
                        break
                    else:
                        print("URL inválida. Intenta de nuevo.")
            elif opcion_modificar == "d" and isinstance(anuncio_a_modificar, Video):
                while True:
                    try:
                        nueva_duracion = int(
                            input("Ingresa la nueva duración del video (segundos): ")
                        )
                        anuncio_a_modificar.duracion = nueva_duracion
                        print("Duración del video actualizada correctamente.")
                        break
                    except ValueError:
                        print("Duración inválida. Ingresa un número entero.")
            elif opcion_modificar in ("d", "e"):  # Salir del bucle de modificación
                break
            else:
                print("Opción inválida. Intenta de nuevo.")
        except SubTipoInvalidoException as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: Ingresa un valor válido.")

    return campana

def main():
    """Función principal del programa."""
    campanas = [] # Lista para almacenar las campañas

    while True:
        print("\n--- Menú Principal ---")
        print("a. Crear campaña")
        print("b. Mostrar campaña")
        print("c. Modificar campaña")
        print("d. Salir")

        opcion = input("Elige una opción: ").lower()

        if opcion == 'a':
            crear_campana(campanas) # Pasar la lista de campañas a la función
        elif opcion == 'b':
            mostrar_campanas(campanas) # Mostrar la lista de campañas
            if campanas:
                while True:
                    try:
                        opcion_campana = int(input("Selecciona el número de la campaña a mostrar: "))
                        if 1 <= opcion_campana <= len(campanas):
                            mostrar_campana(campanas[opcion_campana - 1])
                            break
                        else:
                            print("Opción inválida. Intenta de nuevo.")
                    except ValueError:
                        print("Ingresa un número válido.")
        elif opcion == 'c':
            modificar_campana(campanas) # Pasar la lista de campañas a la función
        elif opcion == 'd':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()