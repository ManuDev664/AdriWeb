import flet as ft
import subprocess

def vista_backup(page, volver_selector):

    def volver(e):
        page.clean()
        volver_selector()

    def crear_tarea(e):
        try:
            # Ejecutar el script con ruta absoluta
            resultado = subprocess.run(
                ["/bin/bash", "/home/dam50/Escritorio/backup.sh"],
                capture_output=True,
                text=True,
                check=True
            )
            mensaje = f"Backup ejecutado correctamente:\n{resultado.stdout}"
            page.snack_bar = ft.SnackBar(ft.Text(mensaje, color=ft.colors.YELLOW), open=True)
        except subprocess.CalledProcessError as err:
            mensaje = f"Error al ejecutar backup.sh:\n{err.stderr}"
            page.snack_bar = ft.SnackBar(ft.Text(mensaje, color=ft.colors.RED), open=True)
        page.update()

    def crear_tarea(e):
        page.snack_bar = ft.SnackBar(ft.Text("Tarea de copia de seguridad creada correctamente.", color=ft.colors.YELLOW))
        page.snack_bar.open = True
        page.update()

    origen_input = ft.TextField(label="Ruta de origen", color=ft.colors.YELLOW)
    destino_input = ft.TextField(label="Ruta de destino", color=ft.colors.YELLOW)
    tiempo_input = ft.TextField(label="¿En cuántos minutos iniciar?", color=ft.colors.YELLOW, keyboard_type=ft.KeyboardType.NUMBER)

    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("REALIZAR COPIA DE SEGURIDAD", size=30, weight="bold", color=ft.colors.YELLOW),
            ft.Container(
                bgcolor="#2f2f2f",
                padding=20,
                border_radius=10,
                content=ft.Column(
                    controls=[
                        origen_input,
                        destino_input,
                        tiempo_input,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton("CREAR TAREA", on_click=crear_tarea, color=ft.colors.YELLOW),
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
