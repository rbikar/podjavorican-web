from flask import Flask, send_from_directory

STATIC_FOLDER = '../public'

app = Flask(__name__, static_folder=STATIC_FOLDER)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../public', path)

@app.route('/api/data')
def dynamic():
    return {'data': 'From Flask backend'}

if __name__ == '__main__':
    app.run(debug=True) # TODO debug via env. var