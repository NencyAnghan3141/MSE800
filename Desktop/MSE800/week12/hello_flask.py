
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_flask():
    return 'Hello, Flask!.'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
