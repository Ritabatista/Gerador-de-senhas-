from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Função para gerar a senha
def generate_password(length, include_symbols, include_numbers, include_uppercase):
    charset = string.ascii_lowercase  # Letras minúsculas
    if include_numbers:
        charset += string.digits  # Números
    if include_symbols:
        charset += string.punctuation  # Símbolos
    if include_uppercase:
        charset += string.ascii_uppercase  # Letras maiúsculas

    # Gerando a senha
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')  # Serve a página HTML

@app.route('/generate-password', methods=['POST'])
def generate_password_route():
    data = request.get_json()  # Recebe os dados do formulário
    length = int(data['length'])
    include_symbols = data['includeSymbols']
    include_numbers = data['includeNumbers']
    include_uppercase = data['includeUppercase']
    
    password = generate_password(length, include_symbols, include_numbers, include_uppercase)
    return jsonify({'password': password})  # Retorna a senha gerada em formato JSON

if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask

