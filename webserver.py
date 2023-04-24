from flask import Flask, render_template, request
import socket
import studentsResultsCSVReader
import calculate
import render
import tempfile
import os

app = Flask(__name__)
sock = socket.socket()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/results', methods=["POST"])
def results():
    file = request.files.get('csv')
    if not file:
        return 'No file given'
    temp = tempfile.mktemp()
    file.save(temp)
    results, err = (
        studentsResultsCSVReader.openStudentsResultsCSV(temp))
    os.remove(temp)
    calculatedResults = calculate.convertToCalculateList(results, err)
    html = render.render(calculatedResults, err)
    return html



def startWebserver(port: int):
    app.run('0.0.0.0', port, debug=True)