
from flask import Flask, jsonify, request

from db import create_tables
from util import *
from routes import  *




if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=True)

