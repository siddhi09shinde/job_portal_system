from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Database Connection
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="job_portal",
        user="postgres",
        password="root",
        port="5432"
    )

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        try:
            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute(
                """INSERT INTO users
                (name, email, password, role)
                VALUES (%s, %s, %s, %s)""",
                (name, email, password, role)
            )

            conn.commit()
            cur.close()
            conn.close()

            return "Registration Successful!"

        except Exception as e:
            return "Error: " + str(e)

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)