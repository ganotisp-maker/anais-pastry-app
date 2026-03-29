import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Ρυθμίσεις Φακέλων
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
DATABASE = 'orders.db'

# Δημιουργία απαραίτητων φακέλων
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Αρχικοποίηση της βάσης δεδομένων του ΑΝΑΪΣ"""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            phone TEXT,
            kilos REAL DEFAULT 0,
            price_per_kilo REAL DEFAULT 0,
            down_payment REAL DEFAULT 0,
            delivery_date TEXT,
            description TEXT,
            image_path TEXT,
            status TEXT DEFAULT 'Pending'
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    # Ταξινόμηση: Πρώτα τα Pending (0) μετά τα Completed (1)
    orders = conn.execute('''
        SELECT * FROM orders 
        ORDER BY CASE WHEN status = 'Pending' THEN 0 ELSE 1 END, 
        delivery_date ASC
    ''').fetchall()
    conn.close()
    return render_template('index.html', orders=orders)

@app.route('/add', methods=['POST'])
def add_order():
    try:
        name = request.form.get('name')
        phone = request.form.get('phone')
        dp = request.form.get('down_payment')
        dp = float(dp) if dp else 0.0
        date = request.form.get('delivery_date')
        desc = request.form.get('description')
        
        file = request.files.get('image')
        fname = ""
        if file and file.filename != '':
            fname = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO orders (customer_name, phone, down_payment, delivery_date, description, image_path) 
            VALUES (?,?,?,?,?,?)
        ''', (name, phone, dp, date, desc, fname))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Σφάλμα κατά την προσθήκη: {e}"

@app.route('/complete/<int:order_id>', methods=['POST'])
def complete_order(order_id):
    try:
        k = request.form.get('final_kilos') or 0
        p = request.form.get('price_per_kilo') or 0
        conn = get_db_connection()
        conn.execute('UPDATE orders SET kilos=?, price_per_kilo=?, status="Completed" WHERE id=?', 
                     (float(k), float(p), order_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Σφάλμα κατά την ολοκλήρωση: {e}"

@app.route('/delete/<int:order_id>')
def delete_order(order_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM orders WHERE id=?', (order_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)