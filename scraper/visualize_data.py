import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

def visualize_data():
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost", user="root", password="your_password", database="scraped_data"
    )
    
    # Query to get the number of quotes per author
    query = "SELECT author, COUNT(*) AS quote_count FROM quotes GROUP BY author"
    df = pd.read_sql(query, conn)
    conn.close()

    # Plot the data
    plt.figure(figsize=(10, 6))
    df.plot(kind='bar', x='author', y='quote_count', legend=False, color='skyblue')
    plt.title('Number of Quotes by Author')
    plt.xlabel('Author')
    plt.ylabel('Quote Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Call this function to visualize the data
visualize_data()
