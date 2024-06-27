from flask import Flask, request, redirect, render_template
import os
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        # Your URL shortening logic here
        short_url = request.host_url + 'shortened'
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<path>')
def redirect_to_url(path):
    # Your redirect logic here
    return redirect('http://example.com')

if __name__ == "__main__":
    app.run(debug=True)
