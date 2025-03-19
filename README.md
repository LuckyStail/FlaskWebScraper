# Flask Web Scraper

## Project Overview

    The Flask Web Scraper is an automated system designed to scrape quotes from the website http://quotes.toscrape.com and store them in a MySQL database. It uses Flask for the web interface, allowing users to view, manage, and export the scraped data. The scraper runs on a schedule and collects new quotes daily, with functionality to export the data in CSV or JSON format.


## Key Features:

- **Automated Scraping: Scrapes quotes from multiple pages of the website.
- **Data Storage: Stores scraped quotes in a MySQL database, preventing duplicates.
- **Web Interface: Built with Flask, allowing users to view, search, and filter the quotes.
- **Data Export: Options to export the data as CSV or JSON files.
- **Scheduled Scraping: Automatically runs the scraper every day at midnight.
- **Pagination Support: Scrapes additional pages beyond the first to collect more data.


### 1. **Automated Scraping** Uses Python’s schedule module to scrape new data daily.

### 2. **MySQL Database Integration** - Stores and manages the scraped quotes in a MySQL database.

### 3. **Web Interface (Flask)** - Displays quotes, provides search and filter options, and allows export of data.

### 4. **Data Export** - Allows users to export the data as CSV or JSON files for easy sharing or analysis.

### 5. **Future Enhancements** - Plans to visualize the data using Matplotlib or Pandas.

## Tools Integrated


## Installation and Setup

### System Requirements

- **OS**: Ubuntu (or compatible Linux distribution)
- **Python**: Python 3.x
- **Required Tools**:
  - **MySQL**: For storing the scraped data.
  - **BeautifulSoup**: For scraping website content.
  - **Flask**: For creating the web interface.
  - **Schedule**: FFor automating the scraping process.
    

### Install Dependencies

1. **BeautifulSoup-Web Scraping**

   Purpose: Parses the HTML of the website and extracts relevant data (quotes, authors).
   Features: Allows for easy navigation and extraction of HTML elements.
   Integration: Used to scrape quotes and related data from the website.

2. **MySQL - Database Storage**
   
    Purpose: Stores scraped data in a structured format, preventing duplicates.
    Features: A relational database used to store quotes and their authors.
    Integration: Stores scraped quotes with unique constraints to avoid duplicates.

3. **Flask - Web Interface**

    Purpose: Provides the web dashboard to display the scraped quotes.
    Features: Simple web framework to build interactive and user-friendly interfaces.
    Integration: Used to serve the Flask web app, displaying and managing scraped data.

4. **chedule - Task Scheduling**

   Purpose: Automates the scraping process, running the scraper at scheduled intervals.
    Features: Schedules tasks to run at a specific time, such as every day at midnight.
    Integration: Used to run the scraper daily without manual intervention.

   
- **Dependencies**:
  - Install Python dependencies using pip.
  - Install necessary tools like Nmap, SQLMap, XSStrike, Metasploit.


1. **Clone the repository**:

git clone https://github.com/LuckyStail/FlaskWebScraper.git
cd FlaskWebScraper


2. **Install Python dependencies:**
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

3. **Set up MySQL Database:**
    mysql -u root -p

    CREATE DATABASE scraped_data;

    USE scraped_data;

    CREATE TABLE IF NOT EXISTS quotes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        text TEXT UNIQUE,
        author TEXT
);

        Running the Project
## Run the scraper manually:

bash
Copy
Edit
python scraper.py
This will scrape the first 5 pages of quotes and store them in the MySQL database.

## Run the Flask Web Application:

bash
Copy
Edit
python app.py

This will start the Flask server and you can access the dashboard at http://localhost:5000.

## Automated Scraping:

The scraper will run automatically every day at midnight. To keep the script running, execute the following:

bash
Copy
Edit
python scraper.py

The scraper will automatically check every minute and run the scraping task when it’s time.



4. **Configure MySQL Connection:**
    Update the database credentials in the scraper.py file with your MySQL username, password, and database name.

## Exporting Data

**CSV Export**: The Flask dashboard allows you to export the scraped quotes to a CSV file

**JSON Export**: Similarly, you can export the quotes as a JSON file for easy data transfer.


## Future Enhancements

1. **Data Visualization**: Visualize the scraped data using Matplotlib or Pandas to display trends like the most       popular authors or themes.

2. **Advanced Searching and Filtering**: Allow more sophisticated querying and filtering options on the web            interface to help users find specific quotes.

3. **User Authentication**: Implement user authentication and authorization to manage access to the dashboard and data.


## File Structure

FlaskWebScraper/
│
├── app.py                     # Flask web application (dashboard)
├── scraper.py                 # Web scraper script
├── requirements.txt           # Python dependencies
├── templates/
│   ├── index.html             # Home page for displaying quotes
│   └── export.html            # Page to export data
├── static/                    # Static files (CSS, JavaScript)
│   └── style.css              # Custom styling for the web interface
├── venv/                      # Virtual environment
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file


## Reporting

    ZeroTrace generates detailed reports in multiple formats:

    JSON: Machine-readable format for further analysis.
    HTML: Human-readable format for viewing in a browser.
    PDF: Portable format suitable for sharing.

    Reports are automatically generated and saved in the scan_results/ directory after each scan. You can customize the report generation by modifying the report_generator.py script


## Conclusion

The Flask Web Scraper is a powerful and flexible web scraping tool that provides an easy-to-use interface for automating the process of collecting quotes from the web. By integrating a MySQL database for storage and Flask for the web interface, it enables users to efficiently scrape, view, and export data, all while running on a scheduled task for daily updates.

## Contributing

    Contributions are welcome! If you would like to improve or add new features to the project:

    1. Fork the repository.
    2. Make your changes.
    3. Submit a pull request.


## License 
    This project is licensed under the MIT License. 



### Explanation of Updates:

## 1 BeautifulSoup

📌 Purpose: Parses and extracts data from HTML.


## 2 Flask

📌 Purpose: Creates the web interface.
   

## 3 MySQL

📌 Purpose: Stores and organizes the scraped data.


## 4 Schedule

📌 Purpose: Automates the scraping process.



Feel free to modify and expand the `README.md` as needed to reflect any additional functionality or updates in your project.
