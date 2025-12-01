# 📚 EcoLibrary Project

Plataforma web desarrollada con Django para la gestión y visualización de un catálogo de libros sostenibles. Este sistema integra servicios de autenticación, gestión de favoritos, una API REST interna y consumo de datos en tiempo real desde una API externa.
siguiendo los estándares de documentacion y buenas prácticas.

---

## 📋 Características Principales

1. **Catálogo Público:** Visualización de libros con diseño responsivo (Bootstrap 5 local).
2. **Gestión de Usuarios:** Registro, Iniciar Sesión y Cerrar Sesión.
3. **Sistema de Favoritos:** Los usuarios registrados pueden agregar/quitar libros de su colección personal.
4. **Integración API Externa (Open Library):** Al ver el detalle de un libro, el sistema consulta automáticamente:
   - Calificación promedio.
   - Editorial.
   - Portada oficial (si no hay una local).
5. **API REST Interna:** Endpoints para listar y gestionar libros (`/api/libros/`), protegidos por permisos de administrador.

---

## 🚀 Instrucciones de Instalación

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

### 1. Clonar el repositorio
Descarga el código fuente o clona el repositorio:
```bash
    git clone <https://github.com/OscarVice1/-EcoLibrary.git>
    cd ecolibrary_project
```
### 2. Crear y activar entorno virtual
Es recomendable usar un entorno virtual para aislar las dependencias del proyecto y evitar conflictos.

```bash
python -m venv venv

# En Windows:
.\venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate
```
### 3. Instalar dependencias
Instala las librerías necesarias (Django, DRF, Requests, Pillow) definidas en el archivo de requisitos:
```
    pip install -r requirements.txt
```
### 4. Preparar base de datos
Una vez instaladas las librerías, aplica las migraciones para crear las tablas en la base de datos local (SQLite):
```
    python manage.py migrate
```
### 5. Entra como Admin

Para facilitar el uso de todas las funciones de la plataforma y la base de datos, se creó un superusuario:

- **Usuario:** `admin`
- **Contraseña:** `admin123`

> **Nota:** Se recomienda probar agregando un libro con título en inglés (ej: *"The Hobbit"*) y el autor con su nombre exacto para ver la integración automática con la API de Open Library.