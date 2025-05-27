import flet as ft
from Backup import vista_backup
from Usuarios import vista_usuarios

def mostrar_selector(page: ft.Page, volver_menu_principal):

    def seleccionar_accion(e):
        page.clean()
        if e.control.data == "backup":
            page.title = "Backup"
            page.add(vista_backup(page, lambda: mostrar_selector(page, volver_menu_principal)))
        elif e.control.data == "usuarios":
            page.title = "Control de Usuarios"
            page.add(vista_usuarios(page, lambda: mostrar_selector(page, volver_menu_principal)))

    page.clean()
    page.title = "Selector de acción"
    page.bgcolor = "#2f2f2f"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    selector = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("SELECCIONA UNA ACCIÓN A REALIZAR", size=30, color=ft.colors.YELLOW, weight="bold"),
            ft.ElevatedButton("Backup", data="backup", on_click=seleccionar_accion, color=ft.colors.YELLOW),
            ft.ElevatedButton("Control de Usuarios", data="usuarios", on_click=seleccionar_accion, color=ft.colors.YELLOW),
            ft.ElevatedButton("Volver al Menú", on_click=lambda e: volver_menu_principal(), color=ft.colors.WHITE)
        ]
    )

    page.add(selector)
