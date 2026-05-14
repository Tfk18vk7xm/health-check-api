from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Health Check API Running!"

@app.route('/health')
def health():
    return {
        "status": "OK"
    }

@app.route('/time')
def time():
    return {
        "server_time": str(datetime.now())
    }

if __name__ == '__main__':
    app.run(debug=True)