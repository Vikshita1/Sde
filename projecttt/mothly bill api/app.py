from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('bills.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return "Welcome to the Monthly Bill API"

@app.route('/api/bills', methods=['GET'])
def get_bills():
    conn = get_db_connection()
    bills = conn.execute('SELECT * FROM bills').fetchall()
    conn.close()
    return jsonify([dict(bill) for bill in bills]), 200

@app.route('/api/bills/<int:bill_id>', methods=['GET'])
def get_bill(bill_id):
    conn = get_db_connection()
    bill = conn.execute('SELECT * FROM bills WHERE id = ?', (bill_id,)).fetchone()
    conn.close()
    if bill is None:
        return jsonify({'error': 'Bill not found'}), 404
    return jsonify(dict(bill)), 200

@app.route('/api/bills', methods=['POST'])
def add_bill():
    new_bill = request.get_json()
    name = new_bill['name']
    amount = new_bill['amount']
    due_date = new_bill['due_date']

    conn = get_db_connection()
    conn.execute('INSERT INTO bills (name, amount, due_date) VALUES (?, ?, ?)',
                 (name, amount, due_date))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Bill added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
