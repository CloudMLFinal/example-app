from flask import Flask, jsonify
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test1')
def test1():  # success response
    return jsonify({'message': 'success'}), 200


@app.route('/test2')
def test2():  # error response
    return jsonify({'message': 'error'}), 400


@app.route('/test3')
def test3():  # timeout response
    time.sleep(10)
    return jsonify({'message': 'timeout'}), 500

if __name__ == '__main__':
    app.run()
