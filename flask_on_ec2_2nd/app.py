from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def head():
    first = 'This is the first condition'
    return render_template('index.html', message=first)


if __name__ == '__main__':
    # app.run(debug=True)  # for localhost
    app.run(host='0.0.0.0', port=80)  # For production
