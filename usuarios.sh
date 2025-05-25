#!/bin/bash

# Mensajes personalizados
AVISO_FIREFOX="No puedes estar navegando en esta franja horaria."
MENSAJE_MOTIVADOR="¡Sigue adelante, estás haciendo un gran trabajo!"
MENSAJE_FINAL="Ya has trabajado suficiente por hoy."

# Función para mostrar notificaciones (requiere `notify-send`)
function mostrar_mensaje() {
    notify-send "ErciTareas" "$1"
}

# Verifica si un proceso está en ejecución
function esta_abierto() {
    pgrep -x "$1" > /dev/null
}

# Nombres de procesos (puedes cambiar según el sistema si son distintos)
NAVEGADOR="firefox"
CALCULADORA="gnome-calculator"

# Comprobamos el estado de Firefox y la Calculadora
esta_abierto "$NAVEGADOR"
FIREFOX_ABIERTO=$?

esta_abierto "$CALCULADORA"
CALCULADORA_ABIERTA=$?

# Lógica de control
if [ "$FIREFOX_ABIERTO" -eq 0 ]; then
    # Firefox está abierto
    mostrar_mensaje "$AVISO_FIREFOX"
    pkill -x "$NAVEGADOR"
    nohup $CALCULADORA > /dev/null 2>&1 &
    mostrar_mensaje "$MENSAJE_MOTIVADOR"

elif [ "$FIREFOX_ABIERTO" -ne 0 ] && [ "$CALCULADORA_ABIERTA" -ne 0 ]; then
    # Ambos cerrados
    nohup $CALCULADORA > /dev/null 2>&1 &
    mostrar_mensaje "$MENSAJE_MOTIVADOR"

elif [ "$FIREFOX_ABIERTO" -ne 0 ] && [ "$CALCULADORA_ABIERTA" -eq 0 ]; then
    # Firefox cerrado, calculadora abierta
    mostrar_mensaje "$MENSAJE_FINAL"
    pkill -x "$CALCULADORA"
    nohup $NAVEGADOR > /dev/null 2>&1 &
fi
