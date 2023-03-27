from flask import Flask, render_template
import string
import random

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

# background process happening without any refreshing


@app.route('/generate-password')
def generate_password():
       password_length = 10
       password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
       return render_template('generate_password.html', password=password)


if __name__ == '__main__':
    app.run(debug=True)
