from flask import Flask, send_from_directory
import os
STATIC_FOLDER = '../public/'

app = Flask(__name__, static_folder=STATIC_FOLDER)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>',)
def serve_static(path):
    print(f'serving {path}')
    return send_from_directory(STATIC_FOLDER, path)

@app.route('/api/data')
def dynamic():
    return {'data': 'From Flask backend'}

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return send_from_directory(STATIC_FOLDER, '404.html'), 404


if __name__ == '__main__':
    app.run(debug=True) # TODO debug via env. var