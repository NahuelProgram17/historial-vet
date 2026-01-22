# 🐾 Historial Vet – Proyecto Final Django

Aplicación web desarrollada en **Python + Django** como proyecto final del Playground.  
Permite gestionar historiales clínicos veterinarios, perfiles de usuario y mensajería interna.

---

## 🚀 Funcionalidades

- Registro, login y logout de usuarios
- Perfil de usuario con:
  - Nombre
  - Apellido
  - Email
  - Avatar
  - Biografía
  - Edición de perfil y cambio de contraseña
- Gestión de historiales clínicos:
  - Crear, listar, ver, editar y eliminar historiales
  - Cada historial contiene:
    - Nombre de la mascota
    - Edad
    - Especie
    - Historial clínico (texto enriquecido con CKEditor)
    - Vacunas (rabia, moquillo y parvovirus con dosis)
    - Imagen
    - Fecha de creación
- Solo el usuario propietario puede editar o eliminar sus historiales
- Mensajería interna entre usuarios
- Vistas Home y About
- Mensajes flash para notificaciones al usuario
- Panel de administración de Django

---

## 🧰 Tecnologías utilizadas

- Python 3.11
- Django 5
- Django CKEditor
- Bootstrap 5
- SQLite (desarrollo)

---

## 📁 Estructura del proyecto

blog_final/
│
├── accounts/
├── core/
├── pages/
├── messenger/
├── templates/
├── static/
├── media/
├── config/
├── manage.py
├── requirements.txt
└── README.md

## ⚙️ Instalación y ejecución

### 1️⃣ Clonar el repositorio
git clone https://github.com/NahuelProgram17/historial-vet.git
cd historial-vet

2️⃣ Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Migraciones
python manage.py makemigrations
python manage.py migrate

5️⃣ Crear superusuario
python manage.py createsuperuser

6️⃣ Ejecutar servidor
python manage.py runserver

Abrir en el navegador:

http://127.0.0.1:8000/

🔐 Accesos y permisos

Las vistas de creación, edición y eliminación requieren autenticación
Cada usuario solo puede modificar sus propios historiales
La mensajería está disponible únicamente para usuarios registrados

📝 Consideraciones

El archivo db.sqlite3 no se incluye en el repositorio
La carpeta media/ está excluida mediante .gitignore
Se utiliza herencia de templates con base.html
Los formularios con imágenes usan enctype="multipart/form-data"

🎥 Video de demostración
El video muestra:
Registro e inicio de sesión
Perfil de usuario
CRUD de historiales clínicos
Mensajería entre usuarios
Navegación general del sitio

👤 Autor
Nahuel Pedreyra
Proyecto Final – Django Playground
