# FlaskWebScraperFlask Web Scraper Project Documentation
Project Overview
This project is a web scraper built using Flask, BeautifulSoup, and MySQL to scrape quotes from a website (http://quotes.toscrape.com), store them in a MySQL database, and display the scraped quotes on a web dashboard. The scraper is automated to run daily using the schedule module.

Technologies Used
Flask: A lightweight web framework for Python to build the web dashboard.
BeautifulSoup: A Python library for parsing HTML and extracting data.
MySQL: A relational database to store the scraped quotes.
schedule: A Python library for scheduling tasks like daily scraping.
pymysql: A MySQL client to interact with the MySQL database.
requests: A library to send HTTP requests and fetch web pages.
Project Features
Scrape Quotes: Scrapes quotes from http://quotes.toscrape.com from multiple pages.
Database Integration: Saves scraped data into a MySQL database (scraped_data).
Web Dashboard: Displays the quotes on a Flask-based web dashboard with search and filter functionality.
Scheduled Scraping: Automatically scrapes quotes daily at midnight using the schedule library.
Data Export: Option to export the scraped data in CSV or JSON format.
Data Visualization: Visualization of data trends such as most common authors using Matplotlib.
File Structure Diagram
graphql
Copy
Edit
FlaskWebScraper/
│
├── app.py               # Main Flask app to run the server and display the dashboard
├── scraper/             # Folder for scraper logic and database functions
│   ├── scraper.py       # Contains functions to scrape data and save to DB
│   └── __init__.py      # Init file for scraper module
├── templates/           # Folder for HTML files used by Flask
│   ├── index.html       # Main dashboard HTML file for displaying quotes
│   ├── add_quote.html   # Template for adding or viewing individual quotes (optional)
│   └── layout.html      # Base layout template (used across pages)
├── static/              # Folder for static files like CSS, JS, and images
│   ├── styles.css       # CSS file for styling the dashboard
│   └── script.js        # Optional JavaScript for interactivity (e.g., filtering)
├── requirements.txt     # Lists all the dependencies for the project
├── .gitignore           # Git ignore file to prevent sensitive and unnecessary files from being committed
└── README.md            # Documentation of the project (this file)
Detailed Explanation of Files
1. app.py (Flask Application)
This file contains the main Flask application code, responsible for setting up routes, rendering HTML templates, and handling user interactions (e.g., searching/filtering quotes).

Routes:

/ - The homepage that displays the scraped quotes.
/add_quote - Optionally, you can add new quotes manually via the dashboard.
/search - Allows the user to search/filter the quotes.
Functions:

fetch_quotes_from_db() - Fetches quotes from the MySQL database to display on the web dashboard.
2. scraper/scraper.py (Scraper Logic)
This file contains the core logic for scraping the quotes from the website and saving them into the MySQL database.

Functions:
scrape_quotes() - Scrapes the quotes from the target website.
save_quotes_to_db() - Saves the scraped quotes to the MySQL database.
scrape_and_save() - Integrates the two functions above to scrape and save the data.
Automated Scraping - Uses schedule to run scrape_and_save() automatically every day at midnight.
3. templates/ (HTML Templates)
index.html: The main HTML file that displays the quotes on the web page in a user-friendly interface.

Includes search and filter functionality.
Renders quotes dynamically using Flask’s template engine.
layout.html: The base layout for the HTML pages, which includes headers, footers, and navigation menus used across all templates.

4. static/ (Static Files)
styles.css: Contains the CSS to style the dashboard and make the interface clean and user-friendly.

script.js: If any JavaScript functionality is added, it can go here, for instance, for dynamic filtering or pagination of quotes.

5. requirements.txt
Contains the list of Python packages required for the project to run, such as:

plaintext
Copy
Edit
Flask==2.1.2
requests==2.26.0
beautifulsoup4==4.10.0
pymysql==1.0.2
schedule==1.1.0
6. .gitignore
This file contains a list of files and directories that should be ignored by Git (e.g., virtual environments, sensitive information). Typical contents include:

plaintext
Copy
Edit
__pycache__/
*.pyc
*.pyo
venv/
*.db
*.sqlite3
.env
7. README.md
This file provides the necessary information for other developers or users to understand the project, how to set it up, and how to use it.

Running the Project
Clone the Repository: If you're cloning from GitHub:

bash
Copy
Edit
git clone https://github.com/yourusername/FlaskWebScraper.git
cd FlaskWebScraper
Set up the Virtual Environment:

Install Python dependencies listed in requirements.txt:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
Set Up MySQL Database:

Ensure MySQL is installed and running.

Create the database:

sql
Copy
Edit
CREATE DATABASE scraped_data;
Run the Flask Application:

Start the Flask app:

bash
Copy
Edit
python app.py
Visit http://localhost:5000 in your web browser to access the web dashboard.

Automate Scraping:

To automatically scrape data daily, ensure the schedule module is running by keeping the script running. You can also run the script in the background or use cron jobs for automation.
Future Enhancements
Data Export: Implement functionality to export scraped quotes to CSV or JSON files.
Data Visualization: Implement data visualization (e.g., common authors, themes) using Matplotlib or Pandas.
User Authentication: Add user login and authentication to protect certain parts of the dashboard.
Error Handling: Enhance error handling to manage failed scraping attempts or database connectivity issues.
