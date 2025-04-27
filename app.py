import os

from flask import Flask, jsonify
import time
import logging

#logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#app
app = Flask(__name__)

#error handler
@app.errorhandler(500)
def handle_500_error(e):
    logger.error(f"Error: {e}")
    return jsonify({'message': 'error'}), 500

@app.route('/')
def hello_world():
    logger.info("[GET] /")
    return 'Hello World!'


@app.route('/test1')
def test1():  # success response
    logger.info("[GET] /test1")
    return jsonify({'message': 'success'}), 200


@app.route('/test2')
def test2():  # error response
    logger.info("[GET] /test2")
    return jsonify({'message': 'error'}), 400

@app.route('/test3')
def test3():  # raise error
    logger.info("[GET] /test3")
    return 1/0


@app.route('/test4')
def test4():  # memory leak
    logger.info("[GET] /test4")
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
