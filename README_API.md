### Curso Técnico de Desenvolvimento de Sistemas - Senai Itapeva  
<h1 align="center">API Flask - Sistema de Clientes da Academia 🔥</h1>

Esta é a API responsável por gerenciar os dados dos clientes da academia. Desenvolvida com **Python e Flask**, ela se comunica com o **Firebase Firestore** e fornece rotas para cadastro, listagem, edição, exclusão, verificação e alteração de status dos clientes. A API está preparada para integração com um frontend via requisições HTTP (CORS habilitado).

## Índice
- [Funcionalidades](#funcionalidades)
- [Endpoints da API](#endpoints-da-api)
- [Tecnologias](#tecnologias)
- [Como executar](#como-executar)
- [Autores](#autores)
- [Status](#status)

## Funcionalidades
- Cadastro de clientes com nome, CPF e status (ativo ou bloqueado)
- Validação de campos obrigatórios e status
- Listagem de todos os clientes
- Edição e exclusão de clientes pelo ID
- Verificação de existência e status do cliente via CPF
- Alteração de status de clientes via requisição PATCH
- Contador automático de ID
- Integração com Firestore (Firebase)
- Suporte a requisições CORS

## Endpoints da API

| Método | Rota                          | Descrição                                  |
|--------|-------------------------------|--------------------------------------------|
| GET    | `/`                           | Verifica se a API está ativa               |
| GET    | `/clientes/lista`            | Lista todos os clientes cadastrados        |
| GET    | `/clientes/<id>`             | Busca cliente pelo ID                      |
| POST   | `/clientes`                  | Adiciona um novo cliente                   |
| PUT    | `/clientes/<id>`            | Altera os dados de um cliente existente    |
| DELETE | `/clientes/<id>`            | Exclui um cliente pelo ID                  |
| POST   | `/clientes/verificar`       | Verifica o status do cliente pelo CPF      |
| PATCH  | `/clientes/<id>/status`     | Atualiza apenas o status do cliente        |

## Tecnologias

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-ffca28?style=for-the-badge&logo=firebase&logoColor=black)
![dotenv](https://img.shields.io/badge/dotenv-000000?style=for-the-badge&logo=dotenv&logoColor=white)

## Como executar

1. Instale as dependências:
   ```bash
   pip install flask firebase-admin python-dotenv flask-cors
   ```

2. Configure a variável de ambiente `CONFIG_FIREBASE` com as credenciais do Firebase (arquivo JSON do serviço).

3. Execute a aplicação:
   ```bash
   python nome_do_arquivo.py
   ```

4. Acesse em `http://localhost:5000/`

## Autores
- Pietro Freire Rezende dos Santos - GitHub - [pietrosantos15](https://github.com/pietrosantos15)
- Thimotio Eduardo Araujo Jeronimo - GitHub - [Thimo08](https://github.com/Thimo08)

## Acessar
Link da Vercel: https://back-seven-mauve.vercel.app/

## Status
✅ Projeto Finalizado ✅