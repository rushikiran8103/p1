from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Database connection parameters
db_user = 'your_db_username'
db_password = 'your_db_password'
db_name = 'your_db_name'
db_host = 'your_db_host'

def get_db_connection():
    return pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)

@app.route('/')
def index():
    # Connect to the database
    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    # Query Users table
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    
    # Query Icon table
    cursor.execute('SELECT * FROM Icon')
    icons = cursor.fetchall()
    
    # Query Publication table
    cursor.execute('SELECT * FROM Publication')
    publications = cursor.fetchall()
    
    # Query UserInteraction table
    cursor.execute('SELECT * FROM UserInteraction')
    user_interactions = cursor.fetchall()
    
    # Query SearchFilter table
    cursor.execute('SELECT * FROM SearchFilter')
    search_filters = cursor.fetchall()
    
    # Query Awards table
    cursor.execute('SELECT * FROM Awards')
    awards = cursor.fetchall()
    
    # Close database connection
    cursor.close()
    connection.close()
    
    # Render index.html template with data
    return render_template('index.html', users=users, icons=icons, publications=publications, 
                           user_interactions=user_interactions, search_filters=search_filters, awards=awards)

if __name__ == '__main__':
    app.run(debug=True)
