bundle exec jekyll build
pip install -r flask-app/requirements.txt
flask run --host=0.0.0.0 --port=$PORT