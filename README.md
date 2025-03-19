Flask Web Scraper Project
Overview
The Flask Web Scraper project is an automated web scraping system that scrapes quotes from the website http://quotes.toscrape.com, stores the data in a MySQL database, and provides a web interface using Flask to display and manage the scraped quotes. The system runs on a schedule, scraping new data daily.

The project includes the following features:

Scraping quotes from multiple pages.
Storing quotes in a MySQL database.
Web interface to view and manage the quotes.
Automation of the scraping process using Python’s schedule module.
Options to export the data as CSV or JSON files.
Features
Automated Scraping: The scraper runs automatically every day at midnight to fetch new quotes and store them in the database.
Web Interface: Built with Flask, the dashboard displays scraped quotes and allows for searching and filtering.
Data Export: Export the scraped quotes in CSV or JSON format for further use.
Database Integration: Uses MySQL to store the quotes with features to prevent duplicates.
Data Visualization (Future): Plans to visualize data trends (e.g., most common authors) using Matplotlib or Pandas.
Installation
Prerequisites
Before you begin, make sure you have the following installed:

Python 3.7+
MySQL server
pip (for installing Python packages)
Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/FlaskWebScraper.git
cd FlaskWebScraper
Create a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
Install required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
Set up the MySQL Database:

Log into MySQL:

bash
Copy
Edit
mysql -u root -p
Create a database:

sql
Copy
Edit
CREATE DATABASE scraped_data;
Create the necessary table if not already created:

sql
Copy
Edit
CREATE TABLE IF NOT EXISTS quotes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text TEXT UNIQUE,
    author TEXT
);
Configure MySQL connection: Update the scraper.py file with your MySQL username, password, and host details.

python
Copy
Edit
conn = pymysql.connect(
    host="localhost",
    user="root",  # your MySQL username
    password="your_password",  # your MySQL password
    database="scraped_data"
)
Running the Project
Run the scraper manually: To run the scraper script, simply execute the following command:

bash
Copy
Edit
python scraper.py
This will scrape the quotes from 5 pages and save them to the database.

Automated Scraping: The scraper is scheduled to run daily at midnight using Python’s schedule module. To keep the scraper running, execute the following command:

bash
Copy
Edit
python scraper.py
The scraper will automatically check every minute and run the scraping task when it’s time.

Run the Flask Web Application: To start the Flask web application, run:

bash
Copy
Edit
python app.py
This will start the web server and you can access the dashboard at http://localhost:5000.

Exporting Data
CSV Export: You can export the scraped data to a CSV file using the export_csv() function in the Flask application.

JSON Export: Similarly, you can export the scraped data to a JSON file using the export_json() function.

Future Enhancements
Data Visualization: We plan to integrate Matplotlib or Pandas to visualize the scraped data, such as plotting the most common authors and themes.

Advanced Searching and Filtering: Future versions will have advanced searching and filtering functionality to better explore the scraped data.

User Authentication: To enhance security and allow users to manage their data, user authentication and authorization will be implemented.

Project Structure
makefile
Copy
Edit
FlaskWebScraper/
│
├── app.py                     # Flask web application (dashboard)
├── scraper.py                 # Web scraper script
├── requirements.txt           # Python package dependencies
├── templates/
│   ├── index.html             # Home page for displaying quotes
│   └── export.html            # Page to export data
├── static/                    # Static files (CSS, JavaScript)
│   └── style.css              # Custom styling for the web interface
├── venv/                      # Virtual environment
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Flask for building the web application.
BeautifulSoup for web scraping.
MySQL for the database integration.
Schedule for automating the scraping process.
