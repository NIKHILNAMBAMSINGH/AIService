import json
from flask import Flask, request, jsonify
import sys
import os

from kafka import KafkaProducer

# Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.app.messageService import MessageService
app = Flask(__name__)
app.config.from_pyfile('config.py')

messageService = MessageService()
producer = KafkaProducer(bootstrap_servers=['3.111.213.48:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
@app.route('/v1/ds/message', methods=['POST'])
def handle_message():
    message = request.json.get('message')

    result = messageService.process_message(message)
    # Convert to dict for both jsonify and Kafka
    result_dict = result.dict()
    # Send to Kafka
    producer.send('expense_service', result_dict)

    return jsonify(result_dict)

@app.route('/', methods=['GET'])
def handle_get():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="localhost", port=7000, debug=True)
