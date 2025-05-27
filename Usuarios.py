import flet as ft
import subprocess

def vista_usuarios(page, volver_selector):

    def volver(e):
        page.clean()
        volver_selector()



    def matar_proceso(e):
        page.snack_bar = ft.SnackBar(ft.Text("Proceso terminado (simulado).", color=ft.colors.YELLOW))
        page.snack_bar.open = True
        page.update()

    pid_input = ft.TextField(label="Introduce PID de proceso a matar", color=ft.colors.YELLOW, keyboard_type=ft.KeyboardType.NUMBER)

    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("CONTROL DE USUARIOS", size=30, weight="bold", color=ft.colors.YELLOW),
            ft.Container(
                bgcolor="#2f2f2f",
                padding=20,
                border_radius=10,
                content=ft.Column(
                    controls=[
                        pid_input,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton("MATAR PROCESO", on_click=matar_proceso, color=ft.colors.YELLOW),
                                ft.ElevatedButton("Volver al selector", on_click=volver, color=ft.colors.YELLOW)
                            ]
                        )
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ]
    )
