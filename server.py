
from flask import Flask, jsonify, request
from flask import Flask, jsonify, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv


# Cargar las variables de entorno
load_dotenv()

# Inicializar la aplicación Flask
app = Flask(__name__)

# Conectar a MongoDB
client = MongoClient(os.getenv('MONGO_URI'))
db = client['tienda']  # Base de datos "tienda"
clientes_collection = db['clientes']  # Colección "clientes"

# Ruta de prueba
@app.route('/')
def home():
    """
    GET /
    Ruta de prueba para verificar la conexión con MongoDB.
    Retorna un mensaje indicando que la conexión fue exitosa.
    """
    return jsonify({"message": "Conexion exitosa con MongoDB"})

# Crear un cliente (POST)
@app.route('/clientes', methods=['POST'])
def crear_cliente():
    """
    POST /clientes
    Crea un nuevo cliente en la base de datos.
    Body JSON:
    {
        "nombre": "Nombre del cliente",
        "email": "Email del cliente",
        "telefono": "Teléfono del cliente",
        "direccion": "Dirección del cliente",
        "productos_comprados": [
            {"producto": "Nombre del producto", "cantidad": 1, "precio": 100}
        ]
    }
    Retorna un mensaje indicando que el cliente fue creado con éxito.
    """
    data = request.json
    nuevo_cliente = {
        "nombre": data.get("nombre"),
        "email": data.get("email"),
        "telefono": data.get("telefono"),
        "direccion": data.get("direccion"),
        "productos_comprados": data.get("productos_comprados", [])
    }
    clientes_collection.insert_one(nuevo_cliente)
    return jsonify({"message": "Cliente creado con éxito"}), 201

# Leer todos los clientes (GET)
@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    """
    GET /clientes
    Obtiene todos los clientes de la base de datos.
    Retorna una lista de clientes.
    """
    clientes = list(clientes_collection.find({}, {"_id": 0}))  # No mostramos el campo "_id"
    return jsonify(clientes), 200

# Leer un cliente por email (GET)
@app.route('/clientes/<email>', methods=['GET'])
def obtener_cliente(email):
    """
    GET /clientes/<email>
    Obtiene un cliente específico basado en su email.
    Parámetros:
    - email: Email del cliente a buscar.
    Retorna los datos del cliente o un mensaje de error si no se encuentra.
    """
    cliente = clientes_collection.find_one({"email": email}, {"_id": 0})
    if cliente:
        return jsonify(cliente), 200
    return jsonify({"message": "Cliente no encontrado"}), 404

# Actualizar un cliente (PUT)
@app.route('/clientes/<email>', methods=['PUT'])
def actualizar_cliente(email):
    """
    PUT /clientes/<email>
    Actualiza los datos de un cliente basado en su email.
    Body JSON con los campos a actualizar:
    {
        "nombre": "Nuevo nombre",
        "telefono": "Nuevo teléfono"
    }
    Retorna un mensaje indicando si la actualización fue exitosa o si el cliente no fue encontrado.
    """
    data = request.json
    resultado = clientes_collection.update_one({"email": email}, {"$set": data})
    if resultado.matched_count:
        return jsonify({"message": "Cliente actualizado con éxito"}), 200
    return jsonify({"message": "Cliente no encontrado"}), 404

# Eliminar un cliente (DELETE)
@app.route('/clientes/<email>', methods=['DELETE'])
def eliminar_cliente(email):
    """
    DELETE /clientes/<email>
    Elimina un cliente basado en su email.
    Parámetros:
    - email: Email del cliente a eliminar.
    Retorna un mensaje indicando si la eliminación fue exitosa o si el cliente no fue encontrado.
    """
    resultado = clientes_collection.delete_one({"email": email})
    if resultado.deleted_count:
        return jsonify({"message": "Cliente eliminado con éxito"}), 200
    return jsonify({"message": "Cliente no encontrado"}), 404

# Nueva ruta para la interfaz web
@app.route('/web')
def web():
    return render_template('index.html')  # Este archivo lo crearemos ahora

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

