from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import time

app = Flask(__name__)
CORS(app)

# Wait for PostgreSQL container
time.sleep(5)

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="taskdb",
    user="postgres",
    password="postgres",
    host="postgres",
    port="5432"
)

# Create table automatically
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL
)
""")

conn.commit()

# Insert sample data if table empty
cur.execute("SELECT COUNT(*) FROM tasks")

count = cur.fetchone()[0]

if count == 0:

    cur.execute("""
    INSERT INTO tasks (title)
    VALUES
    ('Learn Docker'),
    ('Learn Kubernetes'),
    ('Deploy on AWS')
    """)

    conn.commit()

cur.close()

@app.route("/")
def home():
    return jsonify({
        "message": "Cloud DevOps Backend Running Successfully"
    })

@app.route("/tasks")
def get_tasks():

    cur = conn.cursor()

    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1]
        })

    cur.close()

    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)