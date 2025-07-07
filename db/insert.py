import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('link.db')

# Create a cursor object
cur = conn.cursor()

# Create a table with a single integer column 'number'
cur.execute('''
    INSERT INTO episode values (1);
    
''')

# Commit changes and close the connection
conn.commit()
conn.close()
