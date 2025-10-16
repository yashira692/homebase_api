# HomeBase API

HomeBase API es una aplicación desarrollada con Django REST Framework (DRF) que permite gestionar propiedades y propietarios. Cada propiedad está relacionada con un propietario, y se pueden realizar operaciones CRUD completas (crear, listar, editar, eliminar) desde endpoints REST.

# Tecnologías usadas

- Python 3.12+
- Django 5.2.7
- Django REST Framework 3.16.1
- SQLite3 (base de datos por defecto)

# Instrucciones para ejecutar el servidor

Clona o descarga el proyecto
git clone https://github.com/yashira692/homebase_api.git
cd homebase_api
Crea y activa un entorno virtual
python -m venv venv
venv\Scripts\activate
Instala las dependencias
pip install -r requirements.txt
Aplica migraciones
python manage.py makemigrations
python manage.py migrate
Ejecuta el servidor
python manage.py runserver
Abre la API en el navegador
http://127.0.0.1:8000/api/

![curl](image-1.png)
![curl](image.png)

# Endpoints: Propietarios
Listar todos los propietarios
curl http://127.0.0.1:8000/api/owners/

Crear un propietario
curl -X POST http://127.0.0.1:8000/api/owners/ \
-H "Content-Type: application/json" \
-d "{\"nombre\": \"Carlos López\", \"documento\": \"99887766\"}"

Editar un propietario
curl -X PUT http://127.0.0.1:8000/api/owners/1/ \
-H "Content-Type: application/json" \
-d "{\"nombre\": \"Carlos L.\", \"documento\": \"99887766\"}"

Eliminar un propietario
curl -X DELETE http://127.0.0.1:8000/api/owners/1/

# Endpoints: Propiedades
Listar todas las propiedades
curl http://127.0.0.1:8000/api/properties/

Crear una propiedad
curl -X POST http://127.0.0.1:8000/api/properties/ \
-H "Content-Type: application/json" \
-d "{\"titulo\": \"Casa en el centro\", \"direccion\": \"Av. Los Pinos 123\", \"precio\": \"150000.00\", \"tipo\": \"casa\", \"propietario\": 1}"

Editar una propiedad
curl -X PATCH http://127.0.0.1:8000/api/properties/1/ \
-H "Content-Type: application/json" \
-d "{\"precio\": \"155000.00\"}"

Eliminar una propiedad
curl -X DELETE http://127.0.0.1:8000/api/properties/1/
Búsqueda

Filtra propiedades por tipo o título:

curl "http://127.0.0.1:8000/api/properties/?search=casa"


proyecto realizado por yashira rojas alarcon