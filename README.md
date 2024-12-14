# API de Gestión de Clientes - Tienda Electrónica

Esta API permite gestionar clientes en una tienda electrónica. Las funcionalidades incluyen creación, lectura, actualización y eliminación de clientes en una base de datos MongoDB.

## Tecnologías utilizadas

- **Lenguaje**: Python
- **Framework**: Flask
- **Base de datos**: MongoDB (Atlas)
- **Módulos requeridos**: `pymongo`, `flask`, `python-dotenv`

## Configuración inicial

### Requisitos previos

1. Instalar Python 3.6 o superior.
2. Crear un entorno virtual:
   ```bash
   python -m venv env
   ```
3. Activar el entorno virtual:
   - Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source env/bin/activate
     ```
4. Instalar las dependencias necesarias:
   ```bash
   pip install flask pymongo python-dotenv
   ```

### Configuración del entorno

1. Crear un archivo `.env` en el directorio raíz del proyecto.
2. Agregar la siguiente línea al archivo `.env`:
   ```
   MONGO_URI=mongodb+srv://<usuario>:<contraseña>@cluster0.mongodb.net/?retryWrites=true&w=majority
   ```
   Reemplazar `<usuario>` y `<contraseña>` con las credenciales de tu base de datos MongoDB.

## Rutas disponibles

### Ruta de prueba

- **URL**: `/`
- **Método**: `GET`
- **Descripción**: Verifica la conexión con MongoDB.

### Crear un cliente

- **URL**: `/clientes`
- **Método**: `POST`
- **Body JSON**:
  ```json
  {
      "nombre": "Juan Pérez",
      "email": "juan.perez@example.com",
      "telefono": "1234567890",
      "direccion": "Calle Falsa 123",
      "productos_comprados": [
          {"producto": "Laptop", "cantidad": 1, "precio": 15000}
      ]
  }
  ```
- **Respuesta**:
  ```json
  {
      "message": "Cliente creado con éxito"
  }
  ```

### Leer todos los clientes

- **URL**: `/clientes`
- **Método**: `GET`
- **Descripción**: Obtiene una lista de todos los clientes.

### Leer un cliente por email

- **URL**: `/clientes/<email>`
- **Método**: `GET`
- **Descripción**: Obtiene los datos de un cliente específico basado en su email.

### Actualizar un cliente

- **URL**: `/clientes/<email>`
- **Método**: `PUT`
- **Body JSON**: Campos a actualizar.
- **Descripción**: Actualiza la información de un cliente.

### Eliminar un cliente

- **URL**: `/clientes/<email>`
- **Método**: `DELETE`
- **Descripción**: Elimina un cliente específico basado en su email.

## Ejecución

1. Ejecutar el servidor:
   ```bash
   python server.py
   ```
2. Abrir la aplicación en el navegador o consumirla con herramientas como Thunder Client o Postman.

## Créditos

Desarrollado como parte de una práctica para el taller de tecnologías disruptivas por Diana Ruiz Moctezuma


