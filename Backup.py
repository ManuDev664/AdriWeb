import flet as ft
import datetime
import subprocess

def vista_backup(page, volver_selector):

    def volver(e):
        page.clean()
        volver_selector()

    def crear_tarea(e):
        minutos = tiempo_input.value.strip()

        if not minutos.isdigit():
            page.snack_bar = ft.SnackBar(
                ft.Text("Completa correctamente el campo de minutos.", color=ft.Colors.RED),
                open=True
            )
            page.update()
            return

        try:
            minutos = int(minutos)
            tiempo_ejecucion = datetime.datetime.now() + datetime.timedelta(minutes=minutos)

            minuto = tiempo_ejecucion.minute
            hora = tiempo_ejecucion.hour

            # Ruta absoluta del script
            script_path = "/home/dam50/Escritorio/ErciTareasFlet/proyecto.sh"

            # Comando crontab con bash explícito
            cron_line = f"{minuto} {hora} * * * /bin/bash {script_path}\n"

            # Programar tarea en crontab sin eliminar otras
            subprocess.run(f"(crontab -l 2>/dev/null; echo \"{cron_line}\") | crontab -", shell=True)

            page.snack_bar = ft.SnackBar(
                ft.Text("Tarea programada con éxito usando proyecto.sh", color=ft.Colors.GREEN),
                open=True
            )
        except Exception as err:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Error: {str(err)}", color=ft.Colors.RED),
                open=True
            )

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
