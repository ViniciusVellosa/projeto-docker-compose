import os  # <-- Necessário para ler variáveis de ambiente
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    # Lê a variável de ambiente 'AMBIENTE'. 
    # Se ela não existir por algum motivo, usa "Não definido" como padrão.
    ambiente_atual = os.environ.get("AMBIENTE", "Não definido")
    
    return jsonify({
        "service": "backend1",
        "description": "API de usuários",
        "ambiente_execucao": ambiente_atual, # <-- Adiciona a variável na resposta
        "status": "ok"
    })

@app.route("/health")
def health():
    return jsonify({"status": "up"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)