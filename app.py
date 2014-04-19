from flask import Flask, render_template, request, send_from_directory, session, url_for, redirect
import os
import hashlib

app = Flask(__name__)

if os.environ.get('PRODUCTION'):

    app.config.from_object('config.Production')

else:

    app.config.from_object('config.Development')


@app.route('/', methods=['GET', 'POST'])
def home():

    if 'loggedin' not in session:

        return redirect(url_for('login'))

    if request.method == 'POST':

        file = request.files['file']
        extension = file.filename.rsplit('.', 1)[1]

        if file and extension in app.config['ALLOWED']:

            token = os.urandom(4).encode('hex')

            while os.path.isfile(os.path.join(app.config['TARGET'], token + '.' + extension)):

                token = os.urandom(4).encode('hex')

            file.save(os.path.join(app.config['TARGET'], token + '.' + extension))

            return token + '.' + extension, 200

    elif request.method == 'GET':

        return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        if hashlib.sha512(request.form['password']).hexdigest() == app.config['DIGEST']:

        	  session['loggedin'] = os.urandom(30)
        	  return redirect(url_for('home'))

        else:

        	  return redirect(url_for('login'))

    elif request.method == 'GET':

    	  return render_template('login.html')

@app.route('/i/<filename>', methods=['GET'])
def uploads(filename):

    return send_from_directory(app.config['TARGET'], filename)

if __name__ == "__main__":

    app.run(debug=app.config['DEBUG'], port=app.config['PORT'], host=app.config['HOST'])
