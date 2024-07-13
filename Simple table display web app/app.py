from flask import Flask, render_template
import json
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    req = requests.get("https://wolnelektury.pl/api/books/?format=json")
    data = json.loads(req.content)
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run()
