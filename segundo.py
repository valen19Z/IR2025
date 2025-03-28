import flet as ft

# Función principal que maneja la lógica de la página
def main(page: ft.Page):
    # Establecer título de la página
    page.title = "GridView - Imágenes con Audio"
    # Configurar el tema oscuro para la interfaz
    page.theme_mode = ft.ThemeMode.DARK
    # Añadir un margen de 50 píxeles alrededor de la página
    page.padding = 50
    # Centrar los elementos verticalmente en la página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # Centrar los elementos horizontalmente en la página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()  # Actualizar la página para aplicar los cambios

    # Diccionario que asocia imágenes con archivos de audio
    audio_files = {
        "images/sueño.jpg": "audio/sueño.mp3",  # Imagen de sueño con audio de sueño
        "images/calor.jpg": "audio/calor.mp3"   # Imagen de calor con audio de calor
    }

    # Crear un diccionario de objetos de audio, cada uno asociado a un archivo
    audio_players = {key: ft.Audio(src=value, autoplay=False) for key, value in audio_files.items()}
    
    # Función que se ejecuta al hacer clic en la imagen
    def runanimate(e):
        # Si el archivo de audio correspondiente existe, se reproduce
        if e.control.data in audio_players:
            audio_players[e.control.data].play()
        page.update()  # Actualizar la página para reflejar el cambio

    # Crear el contenedor principal donde se agruparán las imágenes
    main_container = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,  # Centrar los elementos horizontalmente
        spacing=100,  # Espacio de 20 píxeles entre los elementos
    )
    
    # Agregar los objetos de audio a la página para que puedan ser reproducidos
    for audio in audio_players.values():
        page.add(audio)
    
    page.add(main_container)  # Añadir el contenedor principal a la página
    
    # Definir una lista de datos de imágenes y títulos con sus colores de borde
    image_data = [
        ("images/sueño.jpg", "Tengo sueño", ft.colors.PURPLE),  # Imagen de sueño con marco violeta
        ("images/calor.jpg", "Tengo calor", ft.colors.YELLOW)   # Imagen de calor con marco amarillo
    ]
    
    # Iterar sobre la lista de imágenes y crear un contenedor para cada una
    for img, title, border_color in image_data:
        main_container.controls.append(  # Añadir cada columna al contenedor principal
            ft.Column(
                controls=[
                    # Agregar un título centrado encima de la imagen
                    ft.Text(title, size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    # Crear un contenedor para la imagen
                    ft.Container(
                        content=ft.Container(  # Contenedor interno que contiene la imagen
                            image_src=img,  # Fuente de la imagen
                            width=400,  # Ancho de la imagen
                            height=400,  # Alto de la imagen
                            ink=True,  # Hace que el contenedor sea clickeable
                            border_radius=ft.border_radius.all(5),  # Bordes redondeados en la imagen
                            on_click=runanimate,  # Al hacer clic, ejecutar la función 'runanimate'
                            data=img  # Guardar la referencia de la imagen (ruta) para saber qué audio reproducir
                        ),
                        # Definir un borde alrededor del contenedor de la imagen
                        border=ft.border.all(15, border_color),  # El color del borde es definido dinámicamente (violeta o amarillo)
                        border_radius=ft.border_radius.all(25),  # Bordes redondeados en el contenedor
                        padding=5,  # Relleno de 5 píxeles dentro del contenedor
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centrar el contenido verticalmente
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar el contenido horizontalmente
            )
        )
    
    page.update()  # Actualizar la página para reflejar todos los cambios

# Ejecutar la aplicación
ft.app(main)
