# podjavorican-web

## intro

Hybrid web-site for folklore group Podjavorican Telc.
Powered by Jekyll and flask.

## how to run local dev env

### jekyll pre-reqs

```bash
ruby -v
gem -v
gcc -v
g++ -v
make -v

gem update
gem install jekyll bundler
```

### run app

```bash
python -m venv .venv
source .venv/bin/activate
pip install -rflask-app/requirements.txt


export FLASK_DEBUG=1
export FLASK_APP=flask-app/app.py
jekyll build -s web -d public 
flask run
```
