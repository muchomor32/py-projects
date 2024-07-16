from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        q = request.form['q']
        url = 'https://www.googleapis.com/books/v1/volumes'
        params = {
            'q': q
        }
        response = requests.get(url, params=params)
        data = response.json()
        totalItems = data['totalItems']
        if 'items' in data and totalItems > 0:
            items = data['items']
            results = []

            for item in items:

                result = {
                    'title': "",
                    'authors': "",
                    'description': "",
                    'infoLink': ""
                }

                if 'title' in item['volumeInfo']:
                    result['title'] = item['volumeInfo']['title']
                if 'authors' in item['volumeInfo']:
                    result['authors'] = item['volumeInfo']['authors']
                if 'description' in item['volumeInfo']:
                    result['description'] = item['volumeInfo']['description']
                if 'infoLink' in item['volumeInfo']:
                    result['infoLink'] = item['volumeInfo']['infoLink']

                results.append(result)

            return render_template('result.html', results=results)
        else:
            return render_template('result.html', results='No result')


if __name__ == "__main__":
    app.run()
