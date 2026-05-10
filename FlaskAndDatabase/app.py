from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return "Flask Running"

# from flask import Flask, request, redirect, render_template
# from database import get_db_connection

# app = Flask(__name__)

# @app.route('/')
# def index():
#     conn = get_db_connection()
#     students = conn.execute('SELECT * FROM students').fetchall()
#     conn.close()
#     return render_template('index.html', students=students)

# @app.route('/add', methods=['GET', 'POST'])
# def add():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         course = request.form['course']

#         conn = get_db_connection()
#         conn.execute('INSERT INTO students (name, email, course) VALUES (?, ?, ?)', (name, email, course))
#         conn.commit()
#         conn.close()

#         return redirect('/')

#     return render_template('add_student.html')

# @app.route('/delete/<int:id>')
# def delete(id):
#     conn = get_db_connection()
#     conn.execute('DELETE FROM students WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()
#     return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/')
# def hello_world():
#     return 'Hello World'

# @app.route('/home')
# def home():
#     return '<h1>Welcome to the Home Page</h1>'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         if username:
#             return redirect(url_for('home'))
#     return """ 
#        <h1>Login Page</h1>
#         <form method="post" action="/login">
#         <input type="text" name="username" placeholder="Enter your username">
#         <input type="submit" value="Login">
#     </form>"""

# @app.route('/dynamic', defaults={'user_input': 'default'})
# @app.route('/dynamic/<user_input>')
# def dynamic(user_input):
#     return f"<h1>The user entered: {user_input}</h1>"

# @app.route('/query')
# def query():
#     hello = request.args.get('hello')
#     world = request.args.get('world')
#     return f"<h1>The query string contains: {hello} & {world}</h1>"

# # if __name__ == '__main__':
# #     app.run()

