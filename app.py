from flask import Flask, request
from flask import render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def my_form():
    if request.method == "POST":
        print request.form['text']

    return render_template('landing.html')

@app.route('/graph')
def my_graph():
    if request.method == "POST":
        print request.form['text']

    query_string = request.query_string    
    print query_string
    return render_template('rip.html')

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    processed_text = text.upper()
    return processed_text

if __name__ == "__main__":
    app.run()
