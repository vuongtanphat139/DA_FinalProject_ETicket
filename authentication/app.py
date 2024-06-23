from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import secrets
import os

app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'])  
app.secret_key = 'key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# MySQL configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'user'

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'phamlehoaiminh2014@gmail.com'
app.config['MAIL_PASSWORD'] = 'nvmc jkyf rsie dwar'
app.config['MAIL_DEFAULT_SENDER'] = 'phamlehoaiminh2014@gmail.com'

mysql = MySQL(app)
mail = Mail(app)

# Define the Users model
class User(db.Model):
    __tablename__ = 'Users'
    
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    FullName = db.Column(db.String(255), nullable=False)
    Gender = db.Column(db.String(10))
    DoB = db.Column(db.Date)
    Phone = db.Column(db.String(20))
    Email = db.Column(db.String(255), nullable=False)
    Address = db.Column(db.String(255))
    CitizenID = db.Column(db.String(255))
    reset_token = db.Column(db.String(255))

    def __repr__(self):
        return f'<User {self.UserName}>'

    def to_dict(self):
        return {
            'UserID': self.UserID,
            'UserName': self.UserName,
            'FullName': self.FullName,
            'Gender': self.Gender,
            'DoB': self.DoB.isoformat() if self.DoB else None,
            'Phone': self.Phone,
            'Email': self.Email,
            'Address': self.Address,
            'CitizenID': self.CitizenID,
            'reset_token': self.reset_token
        }

# Define the UserCompany model
class UserCompany(db.Model):
    __tablename__ = 'UserCompany'
    
    CompanyID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CompanyUserName = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    CompanyFullName = db.Column(db.String(255), nullable=False)
    Phone = db.Column(db.String(20))
    Email = db.Column(db.String(255), nullable=False)
    Address = db.Column(db.String(255))
    reset_token = db.Column(db.String(255))

    def __repr__(self):
        return f'<UserCompany {self.CompanyUserName}>'

    def to_dict(self):
        return {
            'CompanyID': self.CompanyID,
            'CompanyUserName': self.CompanyUserName,
            'CompanyFullName': self.CompanyFullName,
            'Phone': self.Phone,
            'Email': self.Email,
            'Address': self.Address,
            'reset_token': self.reset_token
        }



# @app.route('/check_db', methods=['GET'])
# def check_db():
#     try:
#         cur = mysql.connection.cursor()
#         cur.execute('SELECT 1')
#         cur.close()
#         return jsonify(message="Connected to MySQL database!")
#     except Exception as e:
#         return jsonify(error=str(e)), 500

# @app.route('/', methods=['GET'])
# def home():
#     if 'username' in session:
#         return jsonify(message=f"Hello, {session['username']}!")
#     else:
#         return jsonify(message="Welcome to the API!")

@app.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()
    cur.close()

    users = []
    for row in rows:
        user = {
            "UserID": row[0],
            "UserName": row[1],
            "Password": row[2],
            "FullName": row[3],
            "Gender": row[4],
            "DoB": row[5],
            "Phone": row[6],
            "Email": row[7],
            "Address": row[8],
            "CitizenID": row[9],
            "reset_token": row[10]
        }
        users.append(user)

    return jsonify(users)

@app.route('/user/<userid>', methods=['GET'])
def get_user_by_id(userid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users WHERE UserID = %s", (userid,))
    row = cur.fetchone()
    cur.close()

    if row:
        user = {
            "UserID": row[0],
            "UserName": row[1],
            "Password": row[2],
            "FullName": row[3],
            "Gender": row[4],
            "DoB": row[5],
            "Phone": row[6],
            "Email": row[7],
            "Address": row[8],
            "CitizenID": row[9],
            "reset_token": row[10]
        }
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/username/<username>', methods=['GET'])
def getUserInfoByUsername(username):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users WHERE UserName = %s", (username,))
    row = cur.fetchone()
    cur.close()

    if row:
        user = {
            "UserID": row[0],
            "UserName": row[1],
            "Password": row[2],
            "FullName": row[3],
            "Gender": row[4],
            "DoB": row[5],
            "Phone": row[6],
            "Email": row[7],
            "Address": row[8],
            "CitizenID": row[9],
            "reset_token": row[10]
        }
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/companyusername/<username>', methods=['GET'])
def getCompanyUserInfoByUsername(username):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usercompany WHERE  CompanyUserName = %s", (username,))
    row = cur.fetchone()
    cur.close()

    if row:
        user = {
            "CompanyID": row[0],
            "CompanyUserName": row[1],
            "Password": row[2],
            "CompanyFullName": row[3],
            "Phone": row[4],
            "Email": row[5],
            "Address": row[6]
        }
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/companies', methods=['GET'])
def get_companies():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM UserCompany")
    rows = cur.fetchall()
    cur.close()

    companies = []
    for row in rows:
        company = {
            "CompanyID": row[0],
            "CompanyUserName": row[1],
            "Password": row[2],
            "CompanyFullName": row[3],
            "Phone": row[4],
            "Email": row[5],
            "Address": row[6]
        }
        companies.append(company)

    return jsonify(companies)

@app.route('/company/<companyid>', methods=['GET'])
def get_company_by_id(companyid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM UserCompany WHERE CompanyID = %s", (companyid,))
    row = cur.fetchone()
    cur.close()

    if row:
        company = {
            "CompanyID": row[0],
            "CompanyUserName": row[1],
            "Password": row[2],
            "CompanyFullName": row[3],
            "Phone": row[4],
            "Email": row[5],
            "Address": row[6]
        }
        return jsonify(company)
    else:
        return jsonify({"error": "Company not found"}), 404

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify(error="Username and password are required."), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT UserName, Password FROM Users WHERE UserName = %s", (username,))
    user = cur.fetchone()
    cur.close()

    if user and password == user[1]:
        session['username'] = user[0]
        return data
    else:
        return jsonify(error="Invalid username or password."), 401

@app.route('/login/company', methods=['POST'])
def loginCompany():
    data = request.get_json()
    username = data.get('CompanyUserName')
    password = data.get('password')

    if not username or not password:
        return jsonify(error="Username and password are required."), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT CompanyUserName, Password FROM UserCompany WHERE CompanyUserName = %s", (username,))
    user = cur.fetchone()
    cur.close()

    if user and password == user[1]:
        session['username'] = user[0]
        return data
    else:
        return jsonify(error="Invalid username or password."), 401

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return jsonify(message="Logged out successfully.")

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    fullname = data.get('fullname')
    gender = data.get('gender')
    dob = data.get('dob')
    phone = data.get('phone')
    email = data.get('email')
    address = data.get('address')
    citizenID = data.get('citizenID')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE UserName = %s OR Email = %s", (username, email))
    existing_user = cur.fetchone()

    if existing_user:
        cur.close()
        return jsonify(error="Username or email already exists. Please choose another."), 400

    cur.execute("INSERT INTO users (UserName, Password, FullName, Gender, DoB, Phone, Email, Address, CitizenID) VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (username, password, fullname, gender, dob, phone, email, address, citizenID))

    mysql.connection.commit()
    cur.close()
    return data

@app.route('/registerCompany', methods=['POST'])
def register_company():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    company_fullname = data.get('company_fullname')
    phone = data.get('phone')
    email = data.get('email')
    address = data.get('address')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM UserCompany WHERE CompanyUserName = %s OR Email = %s", (username, email))
    existing_company = cur.fetchone()

    if existing_company:
        cur.close()
        return jsonify(error="Company username or email already exists. Please choose another."), 400

    cur.execute("INSERT INTO UserCompany (CompanyUserName, Password, CompanyFullName, Phone, Email, Address) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (username, password, company_fullname, phone, email, address))

    mysql.connection.commit()
    cur.close()
    return data

@app.route('/profile/user/<userid>', methods=['PUT'])
def update_user(userid):
    data = request.get_json()
    user_id = userid
    new_username = data['username']
    new_fullname = data['fullname']
    new_gender = data['gender']
    new_dob = data['dob']
    new_phone = data['phone']
    new_email = data['email']
    new_address = data['address']
    new_citizenID = data['citizenID']

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE Users 
        SET 
            UserName = %s,
            FullName = %s,
            Gender = %s,
            DoB = %s,
            Phone = %s,
            Email = %s,
            Address = %s,
            CitizenID = %s
        WHERE UserID = %s
    """, (new_username, new_fullname, new_gender, new_dob,
          new_phone, new_email, new_address, new_citizenID, user_id))

    mysql.connection.commit()
    cur.close()
    return data

@app.route('/profile/userCompany/<companyid>', methods=['PUT'])
def update_companyuser(companyid):
    data = request.get_json()
    company_id = companyid
    new_companyusername = data.get('username')
    new_companyfullname = data.get('company_fullname')
    new_phone = data.get('phone')
    new_email = data.get('email')
    new_address = data.get('address')

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE UserCompany
        SET 
            companyusername = %s,
            companyfullname = %s,
            Phone = %s,
            Email = %s,
            Address = %s
        WHERE CompanyID = %s
    """, (new_companyusername, new_companyfullname, new_phone, new_email, new_address, company_id))

    mysql.connection.commit()
    cur.close()
    return data

@app.route('/reset-password/request', methods=['POST'])
def reset_password_request():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify(error="Email is required."), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE Email = %s", (email,))
    user = cur.fetchone()

    if not user:
        cur.execute("SELECT * FROM UserCompany WHERE Email = %s", (email,))
        user = cur.fetchone()
    
    cur.close()

    if not user:
        return jsonify(error="No user found with that email address."), 404

    reset_token = secrets.token_urlsafe(32)
    store_reset_token(email, reset_token)
    send_reset_password_email(email, reset_token)
    return jsonify(message="Password reset instructions sent to your email.")

def store_reset_token(email, reset_token):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET reset_token = %s WHERE Email = %s", (reset_token, email))
    mysql.connection.commit()
    cur.close()

def send_reset_password_email(email, reset_token):
    reset_link = f"http://localhost:5173/resetPassword?token={reset_token}"
    msg = Message('Password Reset Request', recipients=[email])
    msg.body = f"Click the following link to reset your password: {reset_link}"

    try:
        mail.send(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

@app.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    data = request.get_json()
    new_password = data.get('new_password')

    if not new_password:
        return jsonify(error="New password is required."), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE reset_token = %s", (token,))
    user = cur.fetchone()

    if not user:
        return jsonify(error="Invalid or expired token."), 401

    cur.execute("UPDATE users SET Password = %s, reset_token = NULL WHERE reset_token = %s", (new_password, token))
    mysql.connection.commit()
    cur.close()
    return jsonify(message="Password reset successfully.")

# @app.route('/test-email', methods=['GET'])
# def test_email():
#     msg = Message('Test Email', recipients=['phamlehoaiminh2014@gmail.com'])
#     msg.body = 'This is a test email.'
#     try:
#         mail.send(msg)
#         return 'Test email sent successfully!'
#     except Exception as e:
#         return f'Failed to send test email: {str(e)}'

if __name__ == "__main__":
    app.run(debug=True)




