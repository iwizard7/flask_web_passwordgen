from flask import Flask, render_template, request, send_from_directory
import random, os
import string

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route('/', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
        password_length = int(request.form['password_length'])
        complexity = request.form['complexity']

        if complexity == 'easy':
            characters = string.ascii_letters
        elif complexity == 'medium':
            characters = string.ascii_letters + string.digits
        else: # complexity == 'hard'
            characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for i in range(password_length))
        return render_template('index.html', password=password)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)