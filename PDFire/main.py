from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

# Home Route
@app.route('/')
def serve():
    return render_template('index.html')

@app.route('/convert', methods = ['POST'])
def convertToPdf():
    result = request.files
    print(result)
    return render_template('output.html')


# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()