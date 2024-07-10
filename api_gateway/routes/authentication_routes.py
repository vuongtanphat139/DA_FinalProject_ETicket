from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'])  
app.secret_key = 'key'

# SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@db-auth:3306/authentication'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# MySQL configuration
app.config['MYSQL_HOST'] = 'db-auth'  # Docker service name
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_ROOT_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'authentication'
app.config['MYSQL_PORT'] = 3306  # MySQL port

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'phamlehoaiminh2014@gmail.com'
app.config['MAIL_PASSWORD'] = 'kfjf llid uorn vpti'
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

# Define the UserOrganization model
class UserOrganization(db.Model):
    __tablename__ = 'UserOrganization'
    
    OrganizationID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OrganizationUserName = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    OrganizationFullName = db.Column(db.String(255), nullable=False)
    Phone = db.Column(db.String(20))
    Email = db.Column(db.String(255), nullable=False)
    Address = db.Column(db.String(255))
    reset_token = db.Column(db.String(255))

    def __repr__(self):
        return f'<UserOrganization {self.OrganizationUserName}>'

    def to_dict(self):
        return {
            'OrganizationID': self.OrganizationID,
            'OrganizationUserName': self.OrganizationUserName,
            'OrganizationFullName': self.OrganizationFullName,
            'Phone': self.Phone,
            'Email': self.Email,
            'Address': self.Address,
            'reset_token': self.reset_token
        }

@app.route('/check_db', methods=['GET'])
def check_db():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT 1')
        cur.close()
        return jsonify(message="Connected to MySQL database!")
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/', methods=['GET'])
def home():
    if 'username' in session:
        return jsonify(message=f"Hello, {session['username']}!")
    else:
        return jsonify(message="Welcome to the API!")

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
    
@app.route('/organizationusername/<username>', methods=['GET'])
def getOrganizationUserInfoByUsername(username):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM userorganization WHERE  OrganizationUserName = %s", (username,))
    row = cur.fetchone()
    cur.close()

    if row:
        user = {
            "OrganizationID": row[0],
            "OrganizationUserName": row[1],
            "Password": row[2],
            "OrganizationFullName": row[3],
            "Phone": row[4],
            "Email": row[5],
            "Address": row[6]
        }
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/organizations', methods=['GET'])
def get_organizations():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM UserOrganization")
    rows = cur.fetchall()
    cur.close()

    organizations = []
    for row in rows:
        organization = {
            "OrganizationID": row[0],
            "OrganizationUserName": row[1],
            "Password": row[2],
            "OrganizationFullName": row[3],
            "Phone": row[4],
            "Email": row[5],
            "Address": row[6]
        }
        organizations.append(organization)

    return jsonify(organizations)

@app.route('/organization/<organizationid>', methods=['GET'])
def get_organization_by_id(organizationid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM UserOrganization WHERE OrganizationID = %s", (organizationid,))
    row = cur.fetchone()
    cur.close()

    if row:
        organization = {
            "OrganizationID": row[0],
            "OrganizationUserName": row[1],
            "Password": row[2],
            "OrganizationFullName": row[3],
            "Phone": row[4],
            "Email": row[5],
            "Address": row[6]
        }
        return jsonify(organization)
    else:
        return jsonify({"error": "Organization not found"}), 404

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

@app.route('/login/organization', methods=['POST'])
def loginOrganization():
    data = request.get_json()
    username = data.get('OrganizationUserName')
    password = data.get('password')

    if not username or not password:
        return jsonify(error="Username and password are required."), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT OrganizationUserName, Password FROM UserOrganization WHERE OrganizationUserName = %s", (username,))
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

@app.route('/registerOrganization', methods=['POST'])
def register_organization():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    organization_fullname = data.get('organization_fullname')
    phone = data.get('phone')
    email = data.get('email')
    address = data.get('address')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM UserOrganization WHERE OrganizationUserName = %s OR Email = %s", (username, email))
    existing_organization = cur.fetchone()

    if existing_organization:
        cur.close()
        return jsonify(error="Organization username or email already exists. Please choose another."), 400

    cur.execute("INSERT INTO UserOrganization (OrganizationUserName, Password, OrganizationFullName, Phone, Email, Address) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (username, password, organization_fullname, phone, email, address))

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

@app.route('/profile/userOrganization/<organizationid>', methods=['PUT'])
def update_organizationuser(organizationid):
    data = request.get_json()
    organization_id = organizationid
    new_organizationusername = data.get('username')
    new_organizationfullname = data.get('organization_fullname')
    new_phone = data.get('phone')
    new_email = data.get('email')
    new_address = data.get('address')

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE UserOrganization
        SET 
            organizationusername = %s,
            organizationfullname = %s,
            Phone = %s,
            Email = %s,
            Address = %s
        WHERE OrganizationID = %s
    """, (new_organizationusername, new_organizationfullname, new_phone, new_email, new_address, organization_id))

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