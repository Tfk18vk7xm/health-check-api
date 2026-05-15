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
    app.run(host='0.0.0.0', port=5000)


# Installed & Verified git
# Verified python installation
# Create project folder
# Initialized git repository
# Created python virtual environment
# Installed Flask
# Created Flask application
# Ran Flask application locally
# Created .gitignore
# Added fles to git
# Checked git status
# First commit
# Created githyb repository
# Connected local repo to github
#created githb actions CI pipeline
# Added CI pipeline
# Triggered pipeline
# Verified pipeline success
