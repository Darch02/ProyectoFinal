#!/usr/bin/python3.10

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Hola mundo desde el microservicio 1'

@app.route('/enviar', methods=['POST']) 
def datos():
    try:
        # Obtener los datos de la solicitud
        data = request.data.decode('utf-8')

        # Escribir los datos en un archivo llamado "chat.txt"
        with open('../chat.txt', 'a') as file:
            file.write(data + '\n')

        # Devolver una respuesta
        return "Datos recibidos y guardados correctamente"
    except Exception as e:
        return f"Error al procesar la solicitud: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
