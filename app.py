from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gamer.db'
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    # fetch contacts from database and show on the home page
    contacts = Contact.query.all()
    return render_template('index.html', all_contacts = contacts)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        message = request.form['message']

        new_contact = Contact(name=name, subject=subject, message=message)
        db.session.add(new_contact)
        db.session.commit()

        return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
