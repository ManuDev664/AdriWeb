import os
import flet as ft
from crontab import CronTab

def mostrar_tareas(page: ft.Page, volver_a_inicio):
    page.title = "Programa ErciTareas"
    page.clean()
    page.bgcolor = "gray"  # Fondo gris

    dropdown = ft.Dropdown(
        label="Selecciona una tarea",
        options=[
            ft.dropdown.Option("Programar BackUP(Copia de Seguridad)"),
            ft.dropdown.Option("Programar Control para Usuarios"),
        ],
        color="yellow"  # Letras del dropdown en amarillo
    )

    def get_minutos():
        return [ft.dropdown.Option(text=str(i).zfill(2), key=str(i).zfill(2)) for i in range(60)]

    def get_horas():
        return [ft.dropdown.Option(text=str(i).zfill(2), key=str(i).zfill(2)) for i in range(24)]

    hora_ft = ft.Dropdown(label="Hora", width=200, options=get_horas(), color="yellow")
    minuto_ft = ft.Dropdown(label="Minuto", width=200, options=get_minutos(), color="yellow")

    def crear_tarea(e):
        cron = CronTab(user=True)
        hora = hora_ft.value
        minuto = minuto_ft.value
        if dropdown.value == "Programar BackUP(Copia de Seguridad)":
            script_path = os.path.join(os.getcwd(), 'backup_proyectos.sh')
            job = cron.new(command=f'{script_path}')
            job.minute.on(minuto)
            job.hour.on(hora)
            cron.write()
        elif dropdown.value == "Programar Control para Usuarios":
            script_path = os.path.join(os.getcwd(), 'control_usuario.sh')
            job = cron.new(command=f'{script_path} "!Exitoso¡"')
            job.minute.on(minuto)
            job.hour.on(hora)
            cron.write()

    btn_volver = ft.ElevatedButton("🔙 Volver al menú", on_click=volver_a_inicio, bgcolor="gray", color="white")

    page.add(
        ft.Column(
            controls=[
                ft.Text("🛠️ Erci Tareas", size=40, weight="bold", color="yellow"),
                hora_ft,
                minuto_ft,
                dropdown,
                ft.ElevatedButton("Crear tarea", on_click=crear_tarea, bgcolor="red", color="white"),
                btn_volver
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
