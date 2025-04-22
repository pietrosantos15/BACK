from flask import Flask, jsonify, request
import random  # Biblioteca para escolher charadas aleatoriamente
from flask_cors import CORS  # Permite requisições de diferentes origens (Cross-Origin Resource Sharing)
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
CORS(app)  


FBKEY = json.loads(os.getenv('CONFIG_FIREBASE'))


cred = credentials.Certificate(FBKEY)
firebase_admin.initialize_app(cred)

db = firestore.client()  


@app.route('/', methods=['GET'])
def index():
    return 'api on fire 🔥'  

@app.route('/clientes/lista', methods=['GET'])
def listacaademia():
    cpfs = []
    lista = db.collection('cpfs').stream()
    for item in lista:
        data = item.to_dict()
        data["id"] = item.id  
        cpfs.append(data)

    if cpfs:
        return jsonify(cpfs), 200
    else:
        return jsonify({'Erro': 'Nenhum cliente encontrado'}), 404
    
@app.route('/clientes/<id>', methods=['GET'])
def busca(id):
    doc_ref = db.collection('cpfs').document(id)  
    doc = doc_ref.get().to_dict()  

    if doc:
        return jsonify(doc), 200  
    else:
        return jsonify({'Mensagem': 'Cliente não encontrado'}), 404  


@app.route('/clientes', methods=['POST'])
def adicionar_cliente():
    dados = request.json  

    
    if "nome" not in dados or "cpf" not in dados or "status" not in dados:
        return jsonify({'Mensagem': 'Campo nome, CPF e status são obrigatórios'}), 400

    status = dados['status'].lower()

    if status not in ["ativo", "bloqueado"]:
        return jsonify({'Mensagem': 'Status inválido. Use ativo ou bloqueado.'}), 400

    
    # Gerenciamento do contador de ID
    contador_ref = db.collection('controle_id').document('contador')
    contador_doc = contador_ref.get().to_dict()
    ultimo_id = contador_doc.get('id')  
    novo_id = int(ultimo_id) + 1  
    contador_ref.update({'id': novo_id})  

    # Grava a nova charada no Firestore
    db.collection('cpfs').document(str(novo_id)).set({
        "id": novo_id,
        "nome": dados['nome'],
        "cpf": dados['cpf'],
        "status": status
    })
    return jsonify({'mensagem': 'Cliente cadastrado com sucesso'}), 201  

@app.route('/clientes/<id>', methods=['PUT'])
def alterar_cliente(id):
    dados = request.json  

    
    if "nome" not in dados or "cpf" not in dados or "status" not in dados:
        return jsonify({'Mensagem': 'Campo nome, CPF e status são obrigatórios'}), 400

    doc_ref = db.collection('cpfs').document(id)  
    doc = doc_ref.get()

    if doc.exists:
        doc_ref.update({
            'nome': dados['nome'],
            'cpf': dados['cpf'],
            'status': dados['status']
        })
        return jsonify({'Mensagem': 'Dados alterados com sucesso'}), 200  
    else:
        return jsonify({'Mensagem': 'Erro. dados não encontrado'}), 404   

@app.route('/clientes/<id>', methods=['DELETE'])
def excluir_cliente(id):
        

        doc_ref = db.collection('cpfs').document(id)  
        doc = doc_ref.get()  

        if not doc.exists:  
            return jsonify({'mensagem': 'Erro - Cliente não encontrado!'}), 404  

        doc_ref.delete()  
        return jsonify({'mensagem': 'Cliente excluído com sucesso!'}), 200  

@app.route('/clientes/verificar', methods=['POST'])
def verificar_cliente():
    dados = request.json
    cpf = dados.get('cpf')

    if not cpf:
        return jsonify({'mensagem': 'CPF não informado'}), 400

    resultado = db.collection('cpfs').where('cpf', '==', cpf).stream()
    documentos = list(resultado)

    if not documentos:
        return jsonify({'status': 'nao_encontrado'}), 404

    for doc in documentos:
        cliente = doc.to_dict()
        return jsonify({'status': cliente.get('status')}), 200
    
@app.route('/clientes/<id>/status', methods=['PATCH'])
def atualizar_status(id):
    
        data = request.get_json(force=True)
        novo_status = data.get('status')

        if not novo_status:
            return jsonify({'mensagem': 'Status não fornecido'}), 400

        cliente_ref = db.collection('clientes').document(id)
        cliente_ref.update({'status': novo_status})

        return jsonify({'mensagem': 'Status atualizado com sucesso'})




if __name__ == '__main__':
    app.run(debug=True) 