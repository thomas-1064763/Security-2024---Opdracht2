import qrcode, os.path, sys, sqlite3

from flask import (Flask, g, redirect, render_template, request, session, url_for, Response)

# a simple demo dataset will be created.
LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

app = Flask(__name__)
app.secret_key = 'geheimekey'


@app.before_request
def before_request():
    g.user = None


def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


data = "/login"
filename = "login_qr_code.png"
generate_qr_code(data, filename)

@app.route("/")
def index():
    if not g.user:
        return redirect(url_for('home'))


    

@app.route("/home")
def home():
    return render_template(
        "display_student_login.html"
    )

@app.route("/login")
def login():
    return render_template(
        "dashboard.html"
    )

@app.route("/start")
def start():
    return render_template(
        "startpagina.html"
    )

@app.route("/agenda")
def agenda():
    return render_template(
        "agenda.html"
    )


if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)

    
