from flask import Flask, request, render_template
import shutil
import os
import pdfy

app = Flask(__name__)

# Home Route
@app.route('/')
def serve():
    return render_template('index.html')

@app.route('/convert', methods = ['POST'])
def convertToPdf():
    if os.path.exists("static/UPLOADS"):
        shutil.rmtree("static/UPLOADS")
        os.mkdir("static/UPLOADS")
    else:
        os.mkdir("static/UPLOADS")
    files = request.files.getlist("files")
    for file in files:
        file.save(os.path.join('static/UPLOADS', file.filename))
    os.chdir("static/UPLOADS")
    pdfy.pdf()
    if os.path.exists('static/UPLOADS/output.pdf'):
        return render_template("output.html")
    else:
        return '<html><body><h1>Sorry we are down. Please Contact Us.</h1></body></html>'


# main driver function
if __name__ == '__main__':
    app.run()