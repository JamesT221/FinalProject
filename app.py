from flask import Flask, render_template_string
import os

app = Flask(__name__)
counter_file = "/data/requests.txt"

@app.route('/')
def index():
    try:
        with open(counter_file, 'r') as f:
            count = f.read()
    except FileNotFoundError:
        count = "0"

    html = f"""
    <html>
    <head>
        <meta http-equiv='refresh' content='60'>
        <title>Request Counter</title>
    </head>
    <body>
        <h1>Requests in the Last Minute: {count}</h1>
    </body>
    </html>
    """
    return html

@app.route('/ping')
def ping():
    try:
        with open(counter_file, 'r+') as f:
            count = int(f.read() or "0") + 1
            f.seek(0)
            f.write(str(count))
            f.truncate()
    except FileNotFoundError:
        with open(counter_file, 'w') as f:
            f.write("1")
    return "Counted"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)