<p align="center">
  <img src="https://img.icons8.com/color/48/000000/django.png" alt="Django Logo"/>
  <img src="https://img.icons8.com/color/48/000000/python.png" alt="Python Logo"/>
</p>

<h1 align="center">Guía Definitiva de Django</h1>

Bienvenido a este repositorio diseñado para aprender Django de manera profunda y práctica. A diferencia de otras guías, este repositorio contiene **código fuente validado** que acompaña a cada lección, permitiéndote ver cómo funcionan los conceptos en un proyecto real.

## 🚀 ¿Cómo usar este repositorio?

Este repositorio se divide en dos partes principales:

1.  **Guías (`docs/`)**: Documentación detallada paso a paso.
2.  **Código Fuente (`src/`)**: Un proyecto de Django funcional (`curso_django`) que implementa los conceptos explicados.

### 📚 Índice de Contenidos

1.  [Introducción a Django](./docs/01_introduccion.md)
2.  [Configuración del Entorno](./docs/02_configuracion.md)
3.  [Modelos y Bases de Datos (Avanzado)](./docs/03_modelos.md)
4.  [Vistas y URLs (CBVs)](./docs/04_vistas_urls.md)
5.  [Plantillas y Archivos Estáticos](./docs/05_plantillas.md)
6.  [Formularios y Validaciones](./docs/06_formularios.md)
7.  [Administración Profesional](./docs/07_admin.md)
8.  [Temas Avanzados y Optimización](./docs/08_avanzado.md)
9.  [Recursos Adicionales](./docs/recursos.md)

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

---

<p align="center">Hecho con ❤️ para la comunidad de Django.</p>
