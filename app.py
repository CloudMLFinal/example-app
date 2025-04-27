import os
from flask import Flask, jsonify, request
import time
import logging
from logging.handlers import RotatingFileHandler

#logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#app
app = Flask(__name__)

@app.after_request
def log_response_info(response):
    logger.info(f'[{request.method}] {request.url}: {response.status}')
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
    return 1/0

@app.route('/test4')
def test4():
    while True:
        time.sleep(1)
        print("Memory leak")
    return jsonify({'message': 'memory leak'}), 200 

#health check
@app.route('/health')
def health():
    logger.info("[GET] /health")
    return jsonify({'message': 'healthy'}), 200

if __name__ == '__main__':
    app.run()