from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'This is homepage for no path<h1>Welcome</h1>'


@app.route('/about')
def about():
    return '<h1>This is my about page</h1>'


@app.route('/err')
def error():
    return '<h1>Error</h1>'


@app.route('/hello')
def hello():
    return '<h1>Hello Flask</h1>'


@app.route('/admin')
def admin():
    # Below, error is the name of the function, not route
    return redirect(url_for('error'))


if __name__ == '__main__':
    app.run(debug=True)
