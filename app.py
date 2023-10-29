from flask import Flask, render_template, request
from model import mensaje
# Crear una instancia de la aplicación Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
   resultado = None
   if request.method == 'POST':
        dato = request.form['dato']
        key = request.form['key']
        # Aquí podrías procesar los datos recibidos, realizar cálculos, etc.
        # Por ejemplo, en este caso, simplemente se muestra el dato ingresado como resultado.
        resultado = f'El dato ingresado es: {dato}'

   return render_template('index.html', resultado=mensaje(dato, key))





if __name__ == '__main__':
    # Ejecutar la aplicación en modo debug en el localhost en el puerto 5000
    app.run(host='0.0.0.0', debug=True)