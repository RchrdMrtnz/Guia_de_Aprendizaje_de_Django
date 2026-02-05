# Guía de Aprendizaje de Django 🐍

Bienvenido al repositorio oficial de la **Guía de Aprendizaje de Django**. Este proyecto tiene un doble propósito: servir como una referencia teórica completa y proporcionar una implementación práctica y validada de los conceptos aprendidos.

## 📚 Documentación

La documentación completa y estructurada está disponible en nuestro sitio web oficial. Se recomienda seguir la guía desde allí para una mejor experiencia de lectura.

👉 **[Leer la Documentación Completa (Sitio Web)](https://RchrdMrtnz.github.io/Guia_de_Aprendizaje_de_Django/)**

---

## 🏗️ Estructura del Proyecto

El repositorio está organizado en dos componentes principales:

- **`docs/`**: Contiene el código fuente de la documentación estática (HTML, CSS, JS) desplegada en GitHub Pages.
- **`src/`**: Contiene el proyecto Django funcional (`curso_django`) con todo el código de los ejemplos educativos.

### Aplicaciones del Proyecto (`src/`)
- **`conceptos_basicos`**: La aplicación principal donde se implementan los ejemplos de modelos, vistas, ORM y patrones de diseño.
- **`users`**: Implementación de un modelo de usuario personalizado (`CustomUser`).
- **`curso_django`**: Configuración central del proyecto (settings modularizados).

---

## 🛠️ Tecnologías

Este proyecto utiliza un stack moderno y profesional:

- **Backend**: Python 3.12, Django 6.0+, Django REST Framework.
- **Base de Datos**: PostgreSQL 15.
- **Contenedores**: Docker & Docker Compose.
- **Frontend (Docs)**: Tailwind CSS (Modo Oscuro, Tipografía).
- **Herramientas de Calidad**: Flake8, Black, Isort, Pre-commit.

---

## 🚀 Guía de Instalación

Puedes ejecutar el proyecto de dos formas: localmente o utilizando Docker.

### Opción A: Ejecución con Docker (Recomendado)

Esta es la forma más sencilla de levantar el proyecto con todas sus dependencias (incluyendo la base de datos).

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/RchrdMrtnz/Guia_de_Aprendizaje_de_Django.git
    cd Guia_de_Aprendizaje_de_Django
    ```

2.  **Iniciar los servicios:**
    ```bash
    docker-compose up --build
    ```

El sitio estará disponible en `http://localhost:8000`.

### Opción B: Ejecución Local

1.  **Requisitos:** Asegúrate de tener Python 3.12+ y PostgreSQL instalados.

2.  **Configurar el entorno:**
    Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar variables de entorno:**
    Crea un archivo `.env` en la raíz (basado en el ejemplo):
    ```bash
    cp .env.example .env
    ```
    *Asegúrate de ajustar la `DATABASE_URL` en el .env si usas una base de datos local diferente.*

5.  **Ejecutar migraciones y servidor:**
    ```bash
    cd src
    python manage.py migrate
    python manage.py runserver
    ```

---

## ✅ Ejecución de Pruebas

Para garantizar que los ejemplos de código funcionan correctamente, el proyecto incluye un script de validación que ejecuta las pruebas automatizadas.

Para validar el código, ejecuta desde la raíz del proyecto:

```bash
./validar_codigo.sh
```

Esto correrá los tests definidos en `src/conceptos_basicos/tests/`, cubriendo:
- Modelos y relaciones.
- ORM Avanzado (Agregaciones, Q objects).
- API Endpoints.

---

<p align="center">
  Hecho con ❤️ para la comunidad de desarrolladores Django.
</p>
