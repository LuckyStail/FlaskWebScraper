from flask import Flask, render_template, request
import MySQLdb
import math

app = Flask(__name__)

# Database connection
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="Madombolo@007",
    db="scraped_data",
    charset="utf8mb4"
)
cursor = db.cursor()

@app.route('/')
def index():
    search_query = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    quotes_per_page = 10

    # Count total quotes for pagination
    if search_query:
        cursor.execute("SELECT COUNT(*) FROM quotes WHERE text LIKE %s OR author LIKE %s",
                       ('%' + search_query + '%', '%' + search_query + '%'))
    else:
        cursor.execute("SELECT COUNT(*) FROM quotes")

    total_quotes = cursor.fetchone()[0]
    total_pages = math.ceil(total_quotes / quotes_per_page)
    offset = (page - 1) * quotes_per_page

    # Fetch quotes with pagination
    if search_query:
        cursor.execute("SELECT text, author FROM quotes WHERE text LIKE %s OR author LIKE %s LIMIT %s OFFSET %s",
                       ('%' + search_query + '%', '%' + search_query + '%', quotes_per_page, offset))
    else:
        cursor.execute("SELECT text, author FROM quotes LIMIT %s OFFSET %s", (quotes_per_page, offset))

    quotes = cursor.fetchall()
    return render_template('index.html', quotes=quotes, search_query=search_query, page=page, total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)
