from flask import Flask, render_template, request, send_from_directory, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os 
from werkzeug.utils import secure_filename
from flask_frozen import Freezer

app = Flask(__name__)

app.secret_key = 'd4uw0y3'

freezer = Freezer(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'joseinnocent431@gmail.com'
app.config['MAIL_PASSWORD'] = 'voiz bmgp vqbj mozl'
db = SQLAlchemy(app)
mail = Mail(app)


class Tender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255), nullable=False)
    contact_person = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Tender {self.company_name}>'


@app.route('/submit', methods=['POST'])
def submit():
        new_tender = Tender(
            company_name=request.form['company_name'],
            contact_person=request.form['contact_person'],
            email=request.form['email'],
            phone=request.form['phone'],
            message=request.form['message'],
        )
        db.session.add(new_tender)
        db.session.commit()
        
        # Send email notification
        msg = Message('New Tender Submission',
                      sender='joseinnocent431@gmail.com',
                      recipients=['josephodhiambo509@gmail.com'])
        msg.body = f"""
        New tender submission:
        Company Name: {request.form['company_name']}
        Contact Person: {request.form['contact_person']}
        Email: {request.form['email']}
        Phone: {request.form['phone']}
        Message: {request.form['message']}
        """
        mail.send(msg)
        flash("Email Sent successfully")
        return redirect(url_for('index'))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Donate/")
def donate():
    return render_template("donate.html")

@app.route("/About-us/")
def about():
    return render_template("about.html")

@app.route("/Our-impact/")
def impact():
    return render_template("impact.html")

@app.route("/Contact-us/")
def contact():
    return render_template("contact.html")

@app.route("/careers/")
def vacancy():
    return render_template("vacancy.html")

@app.route("/Updates/")
def updates():
    return render_template("news.html")

@app.route("/tenders/")
def tenders():
    return render_template("tender.html")

@app.route("/blogs/")
def blog():
    return render_template("blog.html")

if __name__ == ("__main__"):
    with app.app_context():
        db.create_all()
    freezer.freeze()