from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

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