import flet as ft
import datetime
import subprocess

def vista_backup(page, volver_selector):

    def volver(e):
        page.clean()
        volver_selector()

    def crear_tarea(e):
        origen = origen_input.value.strip()
        destino = destino_input.value.strip()
        minutos = tiempo_input.value.strip()

        if not origen or not destino or not minutos.isdigit():
            page.snack_bar = ft.SnackBar(ft.Text("Completa todos los campos correctamente."), open=True)
            page.update()
            return

        try:
            minutos = int(minutos)
            tiempo_ejecucion = datetime.datetime.now() + datetime.timedelta(minutes=minutos)
            minuto = tiempo_ejecucion.minute
            hora = tiempo_ejecucion.hour

            script_path = "/home/dam50/Escritorio/proyecto.sh"

            # Escapar rutas con espacios
            origen_esc = origen.replace(" ", "\\ ")
            destino_esc = destino.replace(" ", "\\ ")

            cron_line = f'{minuto} {hora} * * * /bin/bash {script_path} "{origen_esc}" "{destino_esc}"\n'
            subprocess.run(f'(crontab -l 2>/dev/null; echo "{cron_line}") | crontab -', shell=True)

            page.snack_bar = ft.SnackBar(ft.Text("Tarea programada con éxito."), open=True)
        except Exception as err:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {str(err)}"), open=True)

        page.update()

    origen_input = ft.TextField(label="Ruta de origen")
    destino_input = ft.TextField(label="Ruta de destino")
    tiempo_input = ft.TextField(label="¿En cuántos minutos iniciar?", keyboard_type=ft.KeyboardType.NUMBER)

    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("REALIZAR COPIA DE SEGURIDAD", size=30, weight="bold"),
            ft.Container(
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
                                ft.ElevatedButton("CREAR TAREA", on_click=crear_tarea),
                                ft.ElevatedButton("Volver al selector", on_click=volver)
                            ]
                        )
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ]
    )
