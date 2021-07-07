from flask_mail import Mail, Message
from flask import Flask, request, render_template
 
app = Flask(__name__)
RECIPIENTS = "tech@iac.ac.il"

# Your Code starts here:

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = '', #should add the relevant mail server
    MAIL_PORT = 0, #should find the relevant port for emails
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = '', #should be added by the candidate
    MAIL_PASSWORD = '' #should be added by the candidate
))

mail = Mail(app)

#Make sure that the function handles errors properly
@app.route('/email', methods= ['POST'])
def email():
    sender = request.form["email"]
    msg = Message(subject = f"{sender} completed the challenge!",body=f"{sender} completed the challenge!", sender=sender, recipients=[RECIPIENTS])
    mail.send(msg)
    #You can change the return statement if you want.
    return "ok"

@app.route('/')
def home():
    return render_template("page.html")

if __name__ == "__main__":
    app.run()