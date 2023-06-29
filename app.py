import sys
from flask import Flask, render_template, request, redirect, url_for
from recipe_scrapers import scrape_me
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            scraper = scrape_me(url)
            ingredients = scraper.ingredients()
            directions = scraper.instructions()
            title = scraper.title()
            return render_template('index.html', ingredients=ingredients, directions=directions, title=title)
        except Exception as e:
            error_message = f"Error: {str(e)}"
            return render_template('index.html', error_message=error_message)

    return render_template('index.html')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)
