import flet as ft
from ErciTareasView import mostrar_ercitareas

def main(page: ft.Page):

    def mostrar_menu_principal():
        page.clean()
        page.title = "ErciTareas"
        page.bgcolor = "black"
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        titulo = ft.Text(
            "Bienvenido al ErciTareas by Manuel Arcos | 1ºDAM",
            size=32,
            weight="bold",
            color="purple",
            text_align="center"
        )

        boton_iniciar = ft.ElevatedButton(
            text="Iniciar ErciTareas",
            bgcolor="red",
            color="white",
            on_click=lambda e: mostrar_ercitareas(page, mostrar_menu_principal)
        )

        page.add(
            ft.Column(
                [titulo, boton_iniciar],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30
            )
        )

    mostrar_menu_principal()

ft.app(target=main, view=ft.WEB_BROWSER, port=30004)
