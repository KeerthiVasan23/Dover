import os
from flask import Flask, render_template, request, send_file


app = Flask(__name__, template_folder='../Dover')

APP_FOLDER = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    for file in request.files.getlist('file'):
        filename="input.csv"
    	destination = "/".join([APP_FOLDER, filename])
    	file.save(destination)
    return render_template("index.html")

@app.route("/download", methods=['POST'])
def download():
    os.system('python script.py')
    return send_file(APP_FOLDER+'/output.csv', as_attachment=True)

if __name__ == "__main__":
    app.run(port=4444, debug=True)
