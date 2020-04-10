from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import requests as rq
import azure.storage.blob
import os


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask Panda!"

if __name__ == '__main__':
    port= os.environ.get('PORT')
    app.run(host='0.0.0.0', debug=False, port=port)
