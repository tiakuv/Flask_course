from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    output = render_template("index.html")
    return output

@app.route('/departures/<departure>')
def show_dep(departure):
    output = render_template("departure.html")
    return output

@app.route('/tours/<id>')
def show_tour():
    output = render_template("tour.html")
    return output

app.run('localhost', 8000)
