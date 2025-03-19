import pymysql
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def save_quotes_to_db(quotes):
    try:
        # Connect to the database
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="Madombolo@007",
            database="scraped_data"
        )
        cursor = conn.cursor()

        # Create the table if it doesn't exist
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
                cursor.execute(
                    "INSERT IGNORE INTO quotes (text, author) VALUES (%s, %s)",
                    (quote['text'], quote['author'])
                )
            except pymysql.Error as e:
                logging.error(f"Error inserting quote {quote['text']} by {quote['author']}: {e}")

        # Commit the transaction
        conn.commit()
        logging.info("Quotes have been successfully saved to the database.")

    except pymysql.Error as e:
        logging.error(f"Error connecting to the database: {e}")

    finally:
        # Close the cursor and connection if they exist
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

