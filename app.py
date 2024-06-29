from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from config import DB_CONFIG, MIKROTIK_CONFIG, MPESA_CONFIG, JWT_SECRET, SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# MySQL database connection
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Routes
@app.route('/')
def index():
    plans = [
        {'name': '5 Minutes', 'price': 2},
        {'name': '1 Hour', 'price': 20},
        {'name': '1 Day', 'price': 200},
        {'name': '1 Week', 'price': 500},
        {'name': '1 Month', 'price': 1500}
    ]
    return render_template('index.html', plans=plans)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor.execute("SELECT id, password FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        
        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            flash('Login successful!', 'success')
            return redirect(url_for('account'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        phone = request.form['phone']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)  

        print(hashed_password)  
        
        cursor.execute("INSERT INTO users (username, phone, password) VALUES (%s, %s, %s)", 
                       (username, phone, hashed_password))
        conn.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/account')
def account():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    cursor.execute("SELECT username, email, phone FROM users WHERE id = %s", (session['user_id'],))
    user = cursor.fetchone()
    
    current_plan = {'name': '1 Hour', 'price': 20}  # Placeholder for current plan, implement actual logic

    return render_template('account.html', user=user, current_plan=current_plan)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/plans')
def plans():
    plans = [
        {'name': '5 Minutes', 'price': 2},
        {'name': '1 Hour', 'price': 20},
        {'name': '1 Day', 'price': 200},
        {'name': '1 Week', 'price': 500},
        {'name': '1 Month', 'price': 1500}
    ]
    return render_template('plans.html', plans=plans)

# Flask route to handle plan purchase
@app.route('/buy-plan/', methods=['GET', 'POST'])
def buy_plan(plan_id, amount):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # Fetch plan details based on plan_id from the database or session
    # This step depends on how you manage plans and their details in your application
    
    if request.method == 'POST':
        # Implement payment logic here
        # For example, you might interact with M-Pesa API or any payment gateway
        
        plan_name = request.form.get('plan_name')
        flash(f'Plan purchase successful! You have bought the {plan_name} plan.', 'success')
        return redirect(url_for('account'))
    
    # Render template with plan details for confirmation
    return render_template('buy_plan.html', plan_id=plan_id, amount=amount)


if __name__ == '__main__':
    app.run(debug=True)
