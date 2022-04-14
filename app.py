import flask
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    with open('index.html', 'r', encoding="utf-8") as f:
        return f.read()


@app.post('/search')
def search():
    import csv
    reader = csv.reader(open('data/data.csv', 'r', encoding="utf-8"))
    for i, line in enumerate(reader):
        print(request.form['year'] + '年' + request.form['month'])
        if line[0].replace(" ", "") == request.form['year'] + '年' + request.form['month'] + '月':
            return flask.jsonify([
                line[int(request.form['area']) + 1],
                line[int(request.form['area']) + 8]
            ])

    return flask.jsonify([])


if __name__ == '__main__':
    app.run(debug=True)
