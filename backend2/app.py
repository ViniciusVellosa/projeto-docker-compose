from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    # Criando uma lista mockada (fictícia) de produtos
    produtos = [
        {"id": 1, "nome": "Notebook Dell", "preco": 4500.00},
        {"id": 2, "nome": "Mouse Sem Fio", "preco": 120.50},
        {"id": 3, "nome": "Teclado Mecânico", "preco": 350.00},
        {"id": 4, "nome": "Monitor Ultrawide", "preco": 1800.00}
    ]
    
    return jsonify({
        "service": "backend2",
        "description": "API de produtos",
        "data": produtos
    })

@app.route("/health")
def health():
    return jsonify({"status": "up"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)