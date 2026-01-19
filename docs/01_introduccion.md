# 1. Introducción a Django

## ¿Qué es Django?
Django es un framework web de alto nivel escrito en Python que fomenta un desarrollo rápido y un diseño limpio y pragmático. Construido por desarrolladores experimentados, se encarga de gran parte de las complicaciones del desarrollo web, por lo que puedes concentrarte en escribir tu aplicación sin necesidad de reinventar la rueda.

### Principales características
*   **Completo ("Batteries included"):** Incluye autenticación, ORM, sitemaps, RSS, y más.
*   **Seguro:** Ayuda a evitar errores de seguridad comunes como SQL Injection, XSS, CSRF.
*   **Escalable:** Usado por sitios como Instagram, Pinterest, y Mozilla.

## Arquitectura MVT (Modelo-Vista-Template)
A diferencia del tradicional MVC (Modelo-Vista-Controlador), Django usa MVT:

1.  **Modelo (Model):** La capa de acceso a datos. Define la estructura de la base de datos.
2.  **Vista (View):** La capa de lógica de negocio. Procesa las peticiones y devuelve respuestas. (Equivalente al "Controlador" en MVC).
3.  **Template:** La capa de presentación. Define cómo se muestran los datos al usuario. (Equivalente a la "Vista" en MVC).

---
[Siguiente: Configuración del Entorno](./02_configuracion.md)
