from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Olá! A aplicação está a funcionar perfeitamente."), 200

@app.route('/status')
def status():
    return jsonify(status="OK", version="1.0"), 200

if __name__ == '__main__':
    # Roda a aplicação na porta 5000
    app.run(host='0.0.0.0', port=5000)