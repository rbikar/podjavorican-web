from flask import Flask, send_from_directory
import os
SITE_DIR = os.path.abspath('public')

app = Flask(__name__, static_folder=SITE_DIR)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>',)
def serve_static(path):
    print(f'serving {path}')
    full_path = os.path.join(SITE_DIR, path)
         
    if os.path.isdir(full_path):
        path = os.path.join(path, 'index.html')

    return send_from_directory(SITE_DIR, path)
@app.route('/api/data')
def dynamic():
    return {'data': 'From Flask backend'}

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return send_from_directory(SITE_DIR, '404.html'), 404


if __name__ == '__main__':
    app.run(debug=True) # TODO debug via env. var