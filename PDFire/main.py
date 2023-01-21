from flask import Flask
from flask import render_template

app = Flask(__name__)

# Home Route
@app.route('/')
def hello_world():
    return render_template('index.html')
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()