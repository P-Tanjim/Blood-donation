from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
from MySQLdb.cursors import DictCursor
from datetime import datetime

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = ''  

app.secret_key = 'IsRatM.M'

mysql = MySQL(app)

@app.route('/') #login 
def index():
    return render_template('index.html')  

@app.route('/signin') #sign in
def signin():
    return render_template('signin.html')

@app.route('/event', methods=['GET', 'POST'])
def event():
    
    cur = mysql.connection.cursor(DictCursor)
    # Fetch only pending requests
    cur.execute("SELECT * FROM event_id")
    details = cur.fetchall()
    cur.close()
    
    return render_template('event.html', details=details)

@app.route('/admin_event', methods=['GET', 'POST'])
def admin_event():
    
    cur = mysql.connection.cursor(DictCursor)
    # Fetch only pending requests
    cur.execute("SELECT * FROM event_if")
    details = cur.fetchall()
    cur.close()
    return render_template('admin_event.html', details=details)


@app.route('/admin_crt_event', methods=['GET', 'POST'])
def admin_crt_event():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        event_id = request.form['event_id']
        address = request.form['address']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        
        cursor = mysql.connection.cursor()

        cursor.execute('INSERT INTO event_id (name, email, number, address, start_date, end_date, event_id) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (name, email, number, address, start_date, end_date, event_id))
        
        cursor.execute('INSERT INTO event_if (name, email, number, event_id, address,  description, start_date, end_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                       (name, email, number, event_id, address,  description, start_date, end_date))
        mysql.connection.commit()
        cursor.close()
        flash("Your event request has been submitted successfully.", "success")
        return redirect(url_for('admin_event'))

    return render_template('admin_crt_event.html')



@app.route('/crt_event', methods=['GET', 'POST'])
def crt_event():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        event_id = request.form['event_id']
        address = request.form['address']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO event_id (name, email, number, address, start_date, end_date, event_id) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (name, email, number, address, start_date, end_date, event_id))


        cursor.execute('INSERT INTO event_if (name, email, number, event_id, address,  description, start_date, end_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                       (name, email, number, event_id, address,  description, start_date, end_date))
        mysql.connection.commit()
        cursor.close()
        flash("Your event request has been submitted successfully.", "success")
        return redirect(url_for('event'))

    return render_template('crt_event.html')


# Sign-In route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        contact_number = request.form['contact_number']
        email = request.form['email']
        city = request.form['city']
        state = request.form['state']
        blood_group = request.form['blood_group']
        address = request.form['address']
        user_id = request.form['user_id']
        password = request.form['password']
        man = request.form.get('role')

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (name, contact_number, email, city, state, blood_group, address, user_id, password, man) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (name, contact_number, email, city, state, blood_group, address, user_id, password, man))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('index'))

    return render_template('signin.html')


# Login route
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE name = %s AND password = %s', (name, password))
        user = cursor.fetchone()
        
        if user:
            session['loggedin'] = True
            session['user_id'] = user['user_id']
            return redirect(url_for('user'))
        else:
            return 'Invalid login credentials!'

    return render_template('index.html')

# Admin Login route
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM admin_login WHERE name = %s AND password = %s', (name, password))
        user = cursor.fetchone()
        
        if user:
            session['loggedin'] = True
            session['password'] = user['password']
            return redirect(url_for('admin_user'))
        else:
            return 'Invalid login credentials!'

    return render_template('admin_login.html')

# (protected route)
@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        return f"Hello, {session['user_id']}!"
    return redirect(url_for('login'))

# donation
@app.route('/donate_blood', methods=['GET', 'POST'])
def donate():
    
    if request.method == 'POST':
        full_name = request.form['full_name']
        address = request.form['address']
        donor_id = request.form['donor_id']
        blood_group = request.form['blood_group']
        age = int(request.form['age'])
        donated_units = request.form['donated_units']
        date_of_donation = request.form['date_of_donation']
        donation_id = request.form['donation_id']
        blood_bank = request.form['blood_bank']

        
        #for age calculating
        if age <= 15 or age >= 60:
            flash("Your age is not perfect for donation", "danger")
            return redirect(url_for('donate_user'))
        
        # If the donor has donated before, check the 3-month gap
        last_donation = date_of_donation

        if last_donation:
            last_donation_date = datetime.strptime(date_of_donation, '%Y-%m-%d').date()  # Convert string to date
            current_donation_date = datetime.today().date()

            # Check if the last donation is less than 3 months from the current donation
            if (current_donation_date - last_donation_date).days < 90:  # 90 days for approximately 3 months
                flash("You cannot donate again within 3 months of your last donation.", "danger")
                return redirect(url_for('donate_user'))

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO donor_id (donation_id, blood_group, donated_units)
            VALUES (%s, %s, %s)
        """, (donation_id, blood_group, donated_units))

        cur.execute(
            """
            INSERT INTO donors 
            (full_name, address, donor_id, blood_group, age, donated_units, date_of_donation, donation_id, blood_bank) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (full_name, address, donor_id, blood_group, age, donated_units, date_of_donation, donation_id, blood_bank)
        )
        mysql.connection.commit()
        cur.close()

        flash("Your donation request has been submitted successfully.", "success")
        return redirect(url_for('donate_user'))

    return render_template('donate_blood.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate_user():
    
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("SELECT * FROM donor_id")
    donor_details = cur.fetchall()
    cur.close()

    return render_template('donate.html', donor_details=donor_details)

# Admin Panel Route
@app.route('/admin_donation', methods=['GET', 'POST'])
def admin():
    
    cur = mysql.connection.cursor(DictCursor)
    # Fetch only pending requests
    cur.execute("SELECT * FROM donors")
    donors = cur.fetchall()
    cur.close()
    return render_template('admin_donation.html', donors=donors)

@app.route('/admin_request', methods=['GET', 'POST'])
def admin_2():
    
    cur = mysql.connection.cursor(DictCursor)
    # Fetch only pending requests
    cur.execute("SELECT * FROM request_if")
    request_details = cur.fetchall()
    cur.close()
    return render_template('admin_request.html', request_details=request_details)


@app.route('/user')
def user():
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM bloods")
    units = cur.fetchall()
    cur.close()

    return render_template('user.html', units=units)

# Admin Action Route
@app.route('/update_donor/<int:donor_id>/<action>', methods=['POST'])
def update_donor(donor_id, action):
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    # Fetch donor details from the donors table
    cur.execute("SELECT * FROM donors WHERE donation_id = %s", (donor_id,))
    donor = cur.fetchone()

    if not donor:
        flash("Donor not found.", "danger")
        return redirect(url_for('admin'))

    if action == 'approve':
        # Add or update units, status in donor_id table
        cur.execute("""
            INSERT INTO donor_id (donation_id, blood_group, donated_units, status)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            status = 'Approved'
        """, (donor['donation_id'], donor['blood_group'], donor['donated_units'], 'Approved'))

        blood_group = donor['blood_group']
        donated_units = donor['donated_units']

        # Fetch the current units for the selected blood group from the database
        cur.execute("SELECT `{}` FROM bloods WHERE id = %s".format(blood_group), (1,))
        current_units = cur.fetchone()[blood_group]

        # Add the donated units to the existing units
        total_units = current_units + donated_units

        # Update the blood group with the new total units in the database
        cur.execute("UPDATE bloods SET `{}` = %s WHERE id = %s".format(blood_group), (total_units, 1))

        # Delete the donor from the donors table
        cur.execute("DELETE FROM donors WHERE donation_id = %s", (donor_id,))

    elif action == 'reject':
        cur.execute("UPDATE donor_id SET status = %s WHERE donation_id = %s", ('Rejected', donor_id))
        cur.execute("DELETE FROM donors WHERE donation_id = %s", (donor_id,))
    else:
        flash("Invalid action.", "danger")
        return redirect(url_for('admin'))

    mysql.connection.commit()
    cur.close()

    flash(f"Donor request {action}ed successfully!", "success")
    return redirect(url_for('admin'))

@app.route('/update_event/<int:event_id>', methods=['POST'])
def update_event(event_id):
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    action = request.form.get('action')  # This will be 'approve' or 'reject'
    
    # Fetch event details from the event table
    cur.execute("SELECT * FROM event_if WHERE event_id = %s", (event_id,))
    event = cur.fetchone()

    if not event:
        flash("Event not found.", "danger")
        return redirect(url_for('admin'))

    if action == 'approve':
        description = request.form['description']
        # Add or update units, status in event_id table
        cur.execute("UPDATE event_id SET status = %s, description = %s WHERE event_id = %s", ('Approved', description, event_id))

        # Delete the donor from the donors table
        cur.execute("DELETE FROM event_if WHERE event_id = %s", (event_id,))

    elif action == 'reject':
        description = request.form['description']
        cur.execute("UPDATE event_id SET status = %s, description = %s WHERE event_id = %s", ('Rejected', description, event_id))
        cur.execute("DELETE FROM event_if WHERE event_id = %s", (event_id,))
    else:
        flash("Invalid action.", "danger")
        return redirect(url_for('admin_event'))

    mysql.connection.commit()
    cur.close()

    flash(f"Event request {action}ed successfully!", "success")
    return redirect(url_for('admin_event'))

@app.route('/update_request/<int:request_id>/<action>', methods=['POST'])
def update_request(request_id, action):
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    # Fetch request details from the request_if table
    cur.execute("SELECT * FROM request_if WHERE request_id = %s", (request_id,))
    request = cur.fetchone()

    if not request:
        flash("Request not found.", "danger")
        return redirect(url_for('admin_2'))

    if action == 'approve':
        # Add or update units,status in request_id table

        cur.execute("UPDATE request_id SET status = %s WHERE request_id = %s", ('Approved', request_id))

        blood_group = request['blood_group']
        units = request['units']

        # Fetch the current units for the selected blood group from the database
        cur.execute("SELECT `{}` FROM bloods WHERE id = %s".format(blood_group), (1,))
        current_units = cur.fetchone()[blood_group]

        # Check if the current units in the blood bank are sufficient
        if current_units < units:
            flash(f"Insufficient blood units for group {blood_group}. Available: {current_units}, Requested: {units}.", "danger")
            cur.close()
            return redirect(url_for('admin_2'))

        # Add the donated units to the existing units
        total_units = current_units - units

        # Update the blood group with the new total units in the database
        cur.execute("UPDATE bloods SET `{}` = %s WHERE id = %s".format(blood_group), (total_units, 1))
        
        # Delete the request from the request table
        cur.execute("DELETE FROM request_if WHERE request_id = %s", (request_id,))
    elif action == 'reject':
        # Delete the request directly if rejected
        cur.execute("UPDATE request_id SET status = %s WHERE request_id = %s", ('Rejected', request_id))
        cur.execute("DELETE FROM request_if WHERE request_id = %s", (request_id,))
    else:
        flash("Invalid action.", "danger")
        return redirect(url_for('admin_2'))

    mysql.connection.commit()
    cur.close()

    flash(f"Request {action}ed successfully!", "success")
    return redirect(url_for('admin_2'))

@app.route('/request', methods=['GET', 'POST'])
def Request():
    
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("SELECT * FROM request_id")
    request_details = cur.fetchall()
    cur.close()

    return render_template('request.html', request_details=request_details)

# donation
@app.route('/request_blood', methods=['GET', 'POST'])
def b_request():
    
    if request.method == 'POST':
        name = request.form['name']
        blood_group = request.form['blood_group']
        number = request.form['number']
        reason = request.form['reason']
        date_of_request = request.form['date_of_request']
        units = request.form['units']
        request_id = request.form['request_id']
        patient_id = request.form['patient_id']
        address = request.form['address']

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO request_id (blood_group, request_id, units, reason)
            VALUES (%s, %s, %s, %s)
        """, (blood_group, request_id, units, reason))

        cur.execute(
            """
            INSERT INTO request_if 
            (name, blood_group, number , reason, date_of_request, units,  request_id, patient_id, address) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (name, blood_group, number, reason, date_of_request, units,  request_id, patient_id, address)
        )
        mysql.connection.commit()
        cur.close()

        flash("Your Request has been submitted successfully.", "success")
        return redirect(url_for('Request'))

    return render_template('request_blood.html')

@app.route('/admin_user', methods=['GET', 'POST'])
def admin_user():
    
    if request.method == 'POST':

        blood_group = request.form['blood_group']
        new_units = int(request.form['unit'])

        
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        # Fetch the current units for the selected blood group from the database
        cur.execute(f"SELECT `{blood_group}` FROM bloods WHERE id = 1")
        current_units = cur.fetchone()[blood_group]

        # Add the new units to the existing units
        total_units = current_units + new_units

        # Update the blood group with the new total units in the database
        cur.execute(f"UPDATE bloods SET `{blood_group}` = %s WHERE id = 1", (total_units,))


        mysql.connection.commit()
        cur.close()
        
        flash('Blood units updated successfully!', 'success')
        return redirect(url_for('admin_user'))

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM bloods")
    units = cur.fetchall()
    cur.close()


    return render_template("admin_user.html", units=units)

@app.route('/donate/search_group', methods=['POST'])
def search_group():
    
    if request.method == 'POST':
        blood_group = request.form['group']

        # Query to get donations based on the selected blood group
        cur = mysql.connection.cursor()
        cur.execute("SELECT donation_id, blood_group, donated_units, status FROM donor_id WHERE blood_group = %s", (blood_group,))
        donor_details = cur.fetchall()

        # Convert the donor_details tuple to a list of dictionaries
        donor_details = [
            {
                'donation_id': donation[0],
                'blood_group': donation[1],
                'donated_units': donation[2],
                'status': donation[3]
            }
            for donation in donor_details
        ]

        # Render the template with the donor details
        return render_template('donate.html', donor_details=donor_details)



if __name__ == "__main__":
    app.run(debug=True)
