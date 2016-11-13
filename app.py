from flask import Flask, request
from flask import jsonify
from flask import render_template
import sentanalysis
import process
#import predict
import os

app = Flask(__name__)

app.config['DEBUG'] = True
grapharr = []

@app.route('/')
def my_form():
    if request.method == "POST":
        print request.form['text']

    return render_template('landing.html')


@app.route('/graph', methods=['POST', 'GET'])
def my_graph():
    #print os.getcwd()
    print request.form['text']
    textInput = request.form['text']
    sentVal= sentanalysis.getScore(textInput)
    sentVal = (sentVal+100.00)/20.00
    grapharr = process.compileArray(textInput)
    grapharr = [float(x) for x in grapharr]
    print grapharr
    print sentVal
    #print params

    # predChange = predict.predicttom(textInput, params)
    # predChange *= 100
    # print predChange
    dvval = sentVal+(sentVal/6.3)
    return render_template('rip.html', sentVal=sentVal, grapharr=grapharr, dvval=dvval)


if __name__ == "__main__":
    app.run()
