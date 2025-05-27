#!/bin/bash

# Verificar que se pasaron dos argumentos
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <ruta_origen> <ruta_destino>"
    exit 1
fi

ORIGEN="$1"
DESTINO="$2"

# Crear la carpeta destino si no existe
mkdir -p "$DESTINO"

# Ejecutar la copia recursiva
cp -r "$ORIGEN"/* "$DESTINO"

# Comprobar si la copia fue exitosa
if [ $? -eq 0 ]; then
    echo "Copia de seguridad realizada con éxito: $ORIGEN -> $DESTINO"
else
    echo "Error al realizar la copia de seguridad."
    exit 2
fi
