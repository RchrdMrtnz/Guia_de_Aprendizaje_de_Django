#!/bin/bash

echo "Ejecutando validación del código..."

cd src
python manage.py test conceptos_basicos

if [ $? -eq 0 ]; then
    echo "✅ Todas las pruebas pasaron exitosamente."
    exit 0
else
    echo "❌ Hubo errores en las pruebas."
    exit 1
fi
