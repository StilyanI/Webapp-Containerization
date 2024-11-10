from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('olympics.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute('''
        DROP TABLE IF EXISTS events
    ''')

    c.execute('''
        DROP TABLE IF EXISTS results
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER,
            place INTEGER,
            team TEXT,
            participant TEXT,
            result TEXT,
            FOREIGN KEY (event_id) REFERENCES events (id)
        )
    ''')
    
    c.execute('INSERT INTO events (name) VALUES (?), (?), (?)',
                 ('Athletics', 'Archery', 'Shooting'))
        
    results_data = [
            (1, 1, 'Italy', 'Lamont Marcell Jacobs', '9.80'),
            (1, 2, 'USA', 'Fred Kerley', '9.84'),
            (1, 3, 'Canada', 'Andre De Grasse', '9.89'),
            (2, 1, 'Turkey', 'Mete Gazoz', ''),
            (2, 2, 'Italy', 'Mauro Nespoli', ''),
            (2, 3, 'Japan', 'Takaharu Furukawa', ''),
            (3, 1, 'Iran', 'Javad Foroughi', '244.8'),
            (3, 2, 'Serbia', 'Damir Mikec', '237.9'),
            (3, 3, 'China', 'Wei Pang', '217.6')
        ]
        
    c.executemany('''
            INSERT INTO results (event_id, place, team, participant, result)
            VALUES (?, ?, ?, ?, ?)
        ''', results_data)
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events').fetchall()
    first_event_results = conn.execute('''
        SELECT * FROM results 
        WHERE event_id = 1 
        ORDER BY place
    ''').fetchall()
    conn.close()
    return render_template('index.html', events=events, initial_results=first_event_results)

@app.route('/get_results/<int:event_id>')
def get_results(event_id):
    conn = get_db_connection()
    results = conn.execute('''
        SELECT place, team, participant, result 
        FROM results 
        WHERE event_id = ? 
        ORDER BY place
    ''', (event_id,)).fetchall()
    conn.close()
    return jsonify([dict(row) for row in results])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
