from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Hola mundo desde el microservicio 2'


@app.route('/mostrar_datos')
def index():
    # Lee el contenido del archivo de texto
    with open('../chat.txt', 'r') as file:
        contenido = file.readlines()

    # Renderiza la plantilla index.html con el contenido del archivo
    return render_template('index.html', contenido=contenido)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5556)
