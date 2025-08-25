from flask import Flask

# Cria uma instância da aplicação Flask.
# O argumento __name__ ajuda o Flask a encontrar
# os recursos do seu projeto.
app = Flask(__name__)

# O decorador @app.route('/') define qual URL
# aciona a função a seguir. Neste caso, é a URL
# principal (a raiz do site).
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Esta linha inicia o servidor de desenvolvimento
# apenas se o script for executado diretamente.
if __name__ == '__main__':
    app.run(debug=True)