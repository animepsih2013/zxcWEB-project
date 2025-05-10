from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(port=8888, host='127.0.0.1', debug=True)
