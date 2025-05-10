import os
from flask import Flask, jsonify, request
import time
import logging
import sys
from logging.handlers import RotatingFileHandler

#logger
# Configure root logger
root = logging.getLogger()
root.setLevel(logging.INFO)  # Set root logger level to INFO

# Create and configure stdout handler
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
handler.setFormatter(formatter)

# Remove any existing handlers to avoid duplicate logs
for h in root.handlers[:]:
    root.removeHandler(h)

# Add our configured handler
root.addHandler(handler)

# Create app logger
logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

#app
app = Flask(__name__)

@app.after_request
def log_response_info(response):
    logger.info(f'[{request.method}] {request.path}: {response.status}')
    return response

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test1')
def test1():
    return jsonify({'message': 'success'}), 200

@app.route('/test2')
def test2():
    return jsonify({'message': 'error'}), 400

@app.route('/test3')
def test3():
    try:
        return 1/0
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed", 400

@app.route('/test4')
def test4():
    while True:
        time.sleep(1)
        print("Memory leak")
    return jsonify({'message': 'memory leak'}), 200 

@app.route('/test5')
def test5():
    user_info = {
        "name": "John",
        "age": 20,
        "email": "john@example.com",
        "phone": {
            "work": "0987654321",
            "mobile": "1122334455"
        },
    }
    return jsonify(user_info["phone"]["home"]), 200


#health check
@app.route('/health')
def health():
    return jsonify({'message': 'healthy'}), 200

if __name__ == '__main__':
    app.run()
