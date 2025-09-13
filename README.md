# Creación de entorno

## Creación del entorno

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

- Reiniciar terminales

### Creación de entorno virtual

uv venv .venv

### Activación del entorno virtual

.venv\Scripts\Activate.ps1

### Instalación de dependencias

uv pip install django

## Creación de proyecto

django-admin startproject config .

## Ejecución del servidor

python manage.py runserver

## Creación de aplicación

python manage.py startapp nombre_de_la_app

- Registrar la aplicación en `config/settings.py`:

## Creación de migraciones

python manage.py makemigrations

## Aplicación de migraciones

python manage.py migrate

## Creación de superusuario

python manage.py createsuperuser