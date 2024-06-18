from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    return redirect("https://calendar.google.com/calendar/u/0?cid=YzYwOWNhNWI3YjRiYmJlZDhiYzg0OWZkN2Y2NjMwZTQ2ZDA0MTFlOGI0N2NhNmI4ZTM4ZWJmMDQ0MmQyMjk4OEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t")

if __name__ == '__main__':
    app.run(debug=True)