from flask import Flask

print("file1.py is executing")

app = Flask(__name__)
@app.route('/hello')
def hello_route():
    return "<h1>Hello from file1.py!</h1>"

if __name__ == "__main__":
    print("Starting Flask server")
    app.run(debug=True)
# print("Inside file1.py")
# print(__name__ )



