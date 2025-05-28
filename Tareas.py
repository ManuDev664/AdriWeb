import subprocess
import flet as ft

def mostrar_ercitareas(page: ft.Page, volver_callback):
    page.clean()
    page.title = "ERCI TAREAS FLET"
    page.window_width = 400
    page.window_height = 600
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

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
                subprocess.run(["/bin/bash", "/home/dam50/Escritorio/ErciTareasFlet/proyectos.sh", origen, destino, frecuencia])
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
            subprocess.run(["ps", "aux"], capture_output=True, text=True)  # Se ejecuta pero no se muestra
        except Exception as ex:
            lista.controls.append(ft.Text(f"Error al listar procesos: {ex}", size=12, color="purple"))

        lista.update()
        page.update()

    def ejecutar_matar(e):
        pid = proceso_pid.value
        if pid:
            subprocess.run(["/bin/bash", "/home/dam50/Escritorio/ErciTareasFlet/usuarios.sh", pid])
            proceso_pid.value = ""
            proceso_pid.update()
            actualizar_procesos(lista_procesos_column)

    def matar_proceso_view():
        return ft.Column([
            ft.Text("Matar Procesos", size=20, weight="bold", color="purple"),
            proceso_pid,
            ft.ElevatedButton("Matar proceso", on_click=ejecutar_matar, bgcolor="black", color="white"),
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

    boton_volver = ft.ElevatedButton("Volver al menú principal", on_click=lambda e: volver_callback())

    page.add(ft.Column([
        boton_volver,
        tab_control
    ]))
