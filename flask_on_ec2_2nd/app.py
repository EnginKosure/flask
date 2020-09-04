from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def head():
    first = 'This is the first condition'
    return render_template('index.html', message=first)


@app.route('/names')
def for_loop():
    names = ['John', 'Marry', 'Nancy', 'Dirk']
    return render_template('names.html', names=names)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80)  # For production
    app.run(debug=True)
