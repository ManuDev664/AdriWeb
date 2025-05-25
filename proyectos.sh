#!/bin/bash

# Verificar si se proporcionó una ruta de destino
if [ -z "$1" ]; then
    echo "❌ Error: Debes proporcionar la ruta de destino como parámetro."
    notify-send "ErciTareas" "❌ Debes indicar la ruta de destino para la copia de seguridad."
    exit 1
fi

# Rutas
PROYECTOS_DIR="$HOME/proyectos"
COPIAS_DIR="$HOME/copias"
DESTINO="$1"

# Crear carpetas si no existen
mkdir -p "$PROYECTOS_DIR"
mkdir -p "$COPIAS_DIR"

# Nombre del archivo de copia con fecha y hora
FECHA=$(date +"%Y-%m-%d_%H-%M-%S")
ARCHIVO_COPIA="backup_proyectos_$FECHA.tar.gz"
RUTA_COPIA="$DESTINO/$ARCHIVO_COPIA"

# Crear la copia comprimida
tar -czf "$RUTA_COPIA" -C "$PROYECTOS_DIR" .

# Verificar si se creó correctamente
if [ $? -eq 0 ]; then
    notify-send "ErciTareas" "✅ Copia de seguridad completada: $ARCHIVO_COPIA"
else
    notify-send "ErciTareas" "❌ Error durante la copia de seguridad"
    exit 1
fi

# Abrir el explorador de archivos en la carpeta de destino
xdg-open "$DESTINO" > /dev/null 2>&1 &
