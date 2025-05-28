import subprocess
import flet as ft
import os

def main(page: ft.Page):
    page.title = "ERCI TAREAS FLET"
    page.window_width = 400
    page.window_height = 600
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # Variables globales para acceso desde on_tabs_changed
    proceso_pid = ft.TextField(label="Introduce el Número de PID a MATAR")
    lista_procesos_column = ft.ListView(expand=True, spacing=5, auto_scroll=True)

    def realizar_backup_view():
        ruta_origen = ft.TextField(label="Ruta de origen")
        ruta_destino = ft.TextField(label="Ruta de destino")
        frecuencia_minutos = ft.TextField(label="PROGRAMAR TAREAS EN MINUTOS")

        def ejecutar_backup(e):
            origen = ruta_origen.value
            destino = ruta_destino.value
            frecuencia = frecuencia_minutos.value
            if origen and destino and frecuencia:
                subprocess.run(["/bin/bash", "/home/dam50/Escritorio/proyectos.sh", origen, destino, frecuencia])
                page.snack_bar = ft.SnackBar(ft.Text("Copia de Seguridad Realizada"), open=True)
                page.update()

        return ft.Column([
            ft.Text("COPIAS DE SEGURIDAD", size=20, weight="bold", color="yellow"),
            ruta_origen,
            ruta_destino,
            frecuencia_minutos,
            ft.ElevatedButton("REALIZAR BACKUP", on_click=ejecutar_backup, bgcolor="green", color="red")
        ], scroll="always")

    def actualizar_procesos(lista):
        lista.controls.clear()
        try:
            # Solo para Linux/Unix
            procesos = subprocess.run(["ps", "aux"], capture_output=True, text=True)

            for p in procesos.stdout.splitlines():
                lista.controls.append(ft.Text(p, size=12))
        except Exception as ex:
            lista.controls.append(ft.Text(f"Ha ocurrido un error al listar los procesos: {ex}", size=12, color="purple"))

        lista.update()
        page.update()

    def ejecutar_matar(e):
        pid = proceso_pid.value
        if pid:
            subprocess.run(["/bin/bash", "/home/dam50/Escritorio/usuarios.sh", pid])
            proceso_pid.value = ""
            proceso_pid.update()
            actualizar_procesos(lista_procesos_column)

    def matar_proceso_view():
        return ft.Column([
            ft.Text("Matar Procesos", size=20, weight="bold", color="purple"),
            proceso_pid,
            ft.ElevatedButton("Matar proceso", on_click=ejecutar_matar, bgcolor="black", color="white"),
            ft.Container(
                lista_procesos_column,
                border=ft.border.all(1),
                padding=10,
                height=300
            )
        ], scroll="always")

    tab_control = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        expand=1
    )
  
    def on_tabs_changed(e):
        if tab_control.selected_index == 0:
            actualizar_procesos(lista_procesos_column)
            page.timer(5.0, lambda: actualizar_procesos(lista_procesos_column))

    tab_control.tabs = [
        ft.Tab(text="Matar Procesos", content=matar_proceso_view()),
        ft.Tab(text="Copia de Seguridad", content=realizar_backup_view())
    ]
    tab_control.on_change = on_tabs_changed

    page.add(tab_control)

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=30004)
