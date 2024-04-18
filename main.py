"""
Flask-приложение для генерации паролей.

Приложение принимает POST-запросы с параметрами 'password_length' и 'complexity'.
На основе этих параметров генерируется пароль заданной длины и сложности.

Параметры:
- password_length - длина пароля.
- complexity - сложность пароля ('easy', 'medium', 'hard').

Возвращает:
HTML-страницу с сгенерированным паролем.
"""

from flask import Flask, render_template, request, send_from_directory
import random
import os
import string

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
 """
 Функция favicon возвращает иконку приложения.

 Иконка находится в директории 'static'.
 """
 return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET', 'POST'])
def password_generator():
 """
 Функция password_generator генерирует пароль на основе параметров запроса.

 Если метод запроса POST, то приложение генерирует пароль на основе параметров 'password_length' и 'complexity'.
 В противном случае возвращается HTML-страница без пароля.
 """
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
 app.run(host='0.0.0.0', port=8080)
