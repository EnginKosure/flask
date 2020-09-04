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

# This is a static route
@app.route('/admin')
def admin():
    # Below, error is the name of the function, not route
    return redirect(url_for('error'))


# This is a dynamic route
# @app.route('/<name>')
# # Write the dynamically changing parameter as func param
# # def greet(name):
# #     return f'Hello {name}'
# def greet(name):
#     greet_format = f'''
# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <title>Greeting Page</title>
#   </head>
#   <body>
#     <h1>Hello {name} </h1>
#     <h1>Welcome to my greeting page</h1>
#   </body>
# </html>
#     '''
#     return greet_format

# Create a function named greet_admin which redirect the request to the greet path with parameter of 'Master Admin' and assign to the route of ('/greet-admin')
@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for('greet', name='Master Admin!!!'))


@app.route('/<name>')
def greet(name):
    return render_template('greet.html', n=name)


@app.route('/list10')
def list10():
    return render_template('list10.html')


if __name__ == '__main__':
    app.run(debug=True)
