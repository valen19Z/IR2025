import flet as ft
from flet import *

def main(page: Page):
    # Reproducir un archivo de audio
    audio = Audio(src="audio/sueño.mp3", autoplay=False)
    
    # Función que se ejecuta al hacer clic en la imagen
    def runanimate(e):

        # Reproducir el audio
        audio.play()
        
        page.update()  # Actualiza la página para reflejar el cambio

    # Crear el contenedor con la imagen
    mycon = Container(
        image_src="images/cansado.png",  # Imagen de fondo
        width=400,
        height=360,
        content=ft.Text('Tengo mucho sueño', size=30, color='white'),  # Texto en el contenedor 
        ink=True,  # Hace que el contenedor sea "clickeable"
        on_click=runanimate,  # Llama a la función runanimate cuando se hace clic
    )
    
    # Agregar el contenedor y el audio a la página
    page.add(mycon, audio)

ft.app(target=main)
