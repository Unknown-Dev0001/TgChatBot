from flask import Flask, request
import os

app = Flask(__name__)

port = int(os.environ.get('PORT', 8000))

@app.route('/')
def index():
    return 'Hello user.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)