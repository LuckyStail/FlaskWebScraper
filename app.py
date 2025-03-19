from flask import Flask, render_template
from scraper.scraper import scrape_quotes  # Import the scraping function

app = Flask(__name__)

# Home route to display scraped data
@app.route('/')
def home():
    quotes = scrape_quotes()  # Scrape quotes
    return render_template('index.html', quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True)
