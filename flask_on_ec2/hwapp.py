from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world'


if __name__ == '__main__':
    # whatever the ip is, if it comes through port 80, host it
    app.run(host='0.0.0.0', port=80)
