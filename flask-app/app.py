from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='../public')

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../public', path)

@app.route('/api/data')
def dynamic():
    return {'data': 'From Flask backend'}

if __name__ == '__main__':
    app.run(debug=True)