from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index.html')
def head():
    return render_template('index.html', number=12)


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
