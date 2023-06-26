from flask import Flask, render_template, request, redirect, url_for
from recipe_scrapers import scrape_me

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        scraper = scrape_me(url)
        ingredients = scraper.ingredients()
        directions = scraper.instructions()

        # Redirect the user to the recipe.html page and pass the scraped data to it
        return redirect(url_for('recipe', ingredients=ingredients, directions=directions))

    return render_template('index.html')


@app.route('/recipe')
def recipe():
    # Get the scraped data from the URL parameters
    ingredients = request.args.getlist('ingredients')
    directions = request.args.get('directions')

    return render_template('recipe.html', ingredients=ingredients, directions=directions)


if __name__ == '__main__':
    app.run(debug=True)
