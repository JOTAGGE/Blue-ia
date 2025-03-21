from flask import Flask, jsonify
from flask_cors import CORS  # Importando o CORS

app = Flask(__name__)
CORS(app)  # Permite CORS para todas as rotas

@app.route('/')
def home():
    return 'Bem-vindo à Blue IA - Backend Python!'

@app.route('/processar_dados', methods=['GET'])
def processar_dados():
    resultado = {"status": "processamento realizado"}
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
