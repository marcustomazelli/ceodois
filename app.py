import os
from flask import Flask, render_template
from calculadora import calculadora_app
from monitorar import monitorar_app

# Cria uma instância do Flask
app = Flask(__name__)

app.register_blueprint(calculadora_app)
app.register_blueprint(monitorar_app)

# Rota principal para renderizar a página inicial


@app.route('/')
def index():
    return render_template('index.html')


# python web server
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
