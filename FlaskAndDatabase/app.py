from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/home')
def home():
    return 'Welcome to the Home Page'

@app.route('/dynamic', defaults={'user_input': 'default'})
@app.route('/dynamic/<user_input>')
def dynamic(user_input):
    return f"<h1>The user entered: {user_input}</h1>"



# if __name__ == '__main__':
#     app.run()

