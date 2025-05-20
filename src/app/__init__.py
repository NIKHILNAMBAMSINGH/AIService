from flask import Flask, request, jsonify
import sys
import os

# Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.app.messageService import MessageService
app = Flask(__name__)
app.config.from_pyfile('config.py')

messageService = MessageService()

@app.route('/v1/ds/message/', methods=['POST'])
def handle_message():
    message = request.json.get('message')
    result = messageService.process_message(message)
    return jsonify(result.dict())

@app.route('/', methods=['GET'])
def handle_get():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="localhost", port=9000, debug=True)
