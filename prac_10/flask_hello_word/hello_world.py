from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def fahrenheit(celsius="0"):
    try:
        return str(celsius_to_fahrenheit(float(celsius)))
    except Exception:
        return ""


def celsius_to_fahrenheit(temp):
    return temp * 1.8 + 32


if __name__ == '__main__':
    app.run()