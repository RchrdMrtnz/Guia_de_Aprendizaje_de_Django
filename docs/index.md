# Guía Definitiva de Django

Bienvenido a este repositorio diseñado para aprender Django de manera profunda y práctica. A diferencia de otras guías, este repositorio contiene **código fuente validado** que acompaña a cada lección, permitiéndote ver cómo funcionan los conceptos en un proyecto real.

## 🚀 ¿Cómo usar esta guía?

Esta documentación se divide en lecciones que cubren desde lo básico hasta temas avanzados. Cada sección está respaldada por código funcional que puedes encontrar en la carpeta `src/` del repositorio.

### 📚 Índice de Contenidos

*   [Introducción a Django](01_introduccion.md)
*   [Configuración del Entorno](02_configuracion.md)
*   [Modelos y Bases de Datos (Avanzado)](03_modelos.md)
*   [Vistas y URLs (CBVs)](04_vistas_urls.md)
*   [Plantillas y Archivos Estáticos](05_plantillas.md)
*   [Formularios y Validaciones](06_formularios.md)
*   [Autenticación y Autorización](09_autenticacion.md)
*   [Administración Profesional](07_admin.md)
*   [Temas Avanzados y Optimización](08_avanzado.md)
*   [Recursos Adicionales](recursos.md)

## 🛠️ Instalación y Ejecución

Para ejecutar el código de ejemplo en tu máquina local:

1.  **Clonar el repositorio:**
    ```bash
    git clone <url-del-repo>
    cd <nombre-del-repo>
    ```

2.  **Crear y activar un entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar migraciones:**
    ```bash
    cd src
    python manage.py migrate
    ```

5.  **Correr el servidor:**
    ```bash
    python manage.py runserver
    ```

## ✅ Validación del Código

Una característica clave de esta guía es que todo el código está validado mediante pruebas automatizadas. Puedes verificar que todo funciona correctamente ejecutando el script de validación:

```bash
# Desde la raíz del repositorio
./validar_codigo.sh
```

Esto ejecutará la suite de pruebas de Django (`tests.py`) para asegurar que los modelos y vistas se comportan como se espera.
