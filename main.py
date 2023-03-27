from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')
    if form.validate_on_submit():
        if 'download' in request.form:
            pass  # do something

        elif 'watch' in request.form:
            pass


if __name__ == '__main__':
    app.run()
