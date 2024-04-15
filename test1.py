import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    user_id = request.form['user_id']
    # Potential security risk: SQL Injection
    query = f"SELECT * FROM users WHERE user_id = '{user_id}'"
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return str(results)

if __name__ == '__main__':
    app.run()
