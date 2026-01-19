# 🐾 Historial Vet

Aplicación web desarrollada en **Python con Django** para la gestión de historiales clínicos de mascotas (perros, gatos, caballos, etc.), con sistema de usuarios, autenticación, perfiles y control de acceso por dueño.

El objetivo del proyecto es permitir que cada usuario pueda registrar y administrar los historiales clínicos de sus propias mascotas de forma segura y organizada.

---

## 🚀 Funcionalidades principales

- Registro y autenticación de usuarios
- Perfil de usuario editable
- Creación, edición y eliminación de historiales clínicos
- Asociación de historiales a un usuario (seguridad por propietario)
- Carga de imágenes de mascotas
- Editor de texto enriquecido para el historial clínico (CKEditor)
- Mensajes de confirmación (crear, editar, eliminar)
- Navegación clara con Navbar
- Páginas informativas: Home y About
- Panel de administración (Django Admin)

---

## 🔐 Seguridad

- Acceso restringido mediante login
- Cada usuario solo puede ver, editar y eliminar **sus propios historiales**
- Protección CSRF en formularios
- Uso de `LoginRequiredMixin` y filtrado por usuario (`owner`)

---

## 🛠️ Tecnologías utilizadas

- **Python 3.11**
- **Django**
- **SQLite3** (entorno de desarrollo)
- **Bootstrap 5**
- **django-ckeditor**
- HTML5 / CSS3

---

## 📁 Estructura del proyecto

```bash
historial-vet/
│
├── accounts/        # Autenticación, registro y perfil de usuario
├── pages/           # Historiales clínicos (CRUD)
├── core/            # Home y About
├── messenger/       # Sistema de mensajería (en desarrollo)
├── templates/       # Templates HTML
├── static/          # Archivos estáticos
├── config/          # Configuración del proyecto
├── manage.py
└── requirements.txt

⚙️ Instalación y uso
1️⃣ Clonar el repositorio
git clone https://github.com/NahuelProgram17/historial-vet.git
cd historial-vet

2️⃣ Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Migraciones
python manage.py migrate

5️⃣ Crear superusuario
python manage.py createsuperuser

6️⃣ Ejecutar el servidor
python manage.py runserver