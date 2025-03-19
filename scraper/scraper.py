import requests
from bs4 import BeautifulSoup
import pymysql
import warnings
import schedule
import time

# Ignore warnings from PyMySQL
warnings.filterwarnings("ignore", category=pymysql.Warning)

# Function to scrape quotes
def scrape_quotes():
    base_url = 'http://quotes.toscrape.com/page/{}/'
    quotes = []

    # Loop through pages to scrape quotes
    for page in range(1, 6):  # Scrape 5 pages as an example
        url = base_url.format(page)
        print(f"Scraping page {page}...")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all quote containers on the page
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            quotes.append({"text": text, "author": author})

    print(f"Scraping complete. Found {len(quotes)} quotes")
    return quotes

# Function to save quotes to MySQL database
def save_quotes_to_db(quotes):
    try:
        # Database connection
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="Madombolo@007",  # Make sure this is correct
            database="scraped_data"
        )
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            text TEXT UNIQUE,
            author TEXT
        )
        """)

        # Insert each quote into the database
        for quote in quotes:
            try:
                cursor.execute("INSERT IGNORE INTO quotes (text, author) VALUES (%s, %s)", 
                               (quote['text'], quote['author']))
            except pymysql.Error as e:
                print(f"Error inserting quote '{quote['text']}' by {quote['author']}: {e}")

        conn.commit()
        print(f"Quotes have been successfully saved to the database.")

    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Function to run the scraper and save data
def scrape_and_save():
    print("Starting the scraping process...")
    quotes = scrape_quotes()  # Scrape the quotes from 5 pages
    save_quotes_to_db(quotes)  # Save the quotes to MySQL database
    print("Quotes have been successfully scraped and saved to the database.")

# Schedule the scraper to run every day at midnight
schedule.every().day.at("00:00").do(scrape_and_save)

# Main function to keep the script running and executing scheduled tasks
if __name__ == "__main__":
    print("Starting scraper and scheduler...")
    while True:
        try:
            schedule.run_pending()
            time.sleep(60)  # Wait a minute before checking again
        except Exception as e:
            print(f"Error while running scheduled task: {e}")
            time.sleep(60)  # Wait a minute before retrying
