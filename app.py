from flask import Flask
from flask_mail import Mail, Message

# handle environment variables
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


app.config['DEBUG'] = True
# app.config['MAIL_DEBUG'] = True

app.config['TESTING'] = False
# app.config['MAIL_SUPRESS_SEND'] = False # when testing don't send mails

# change this based on the email domain 
app.config['MAIL_SERVER']='smtp.mailtrap.io'

# depends on the email client provider
app.config['MAIL_PORT'] = 2525 # change this based on the email client, e.g. gmail has 465

# for security and encryption
app.config['MAIL_USE_TLS'] = True

# secure Sockets Layer
app.config['MAIL_USE_SSL'] = False

app.config['MAIL_USERNAME'] = os.getenv("SECRET_MAIL_USERNAME")

app.config['MAIL_PASSWORD'] = os.getenv("SECRET_MAIL_PASSWORD")

# the email comes from..
# if none then use the default sender
# app.config['MAIL_DEFAULT_SENDER'] = None # same as mail_username

# restrict the number of emails sent
# app.config['MAIL_MAX_EMAILS'] = None

# convert attached filenames from unicode to ascii
# app.config['MAIL_ASCII_ATTACHMENTS'] = False


# initialize 
'''
mail = Mail()
mail.init_app(app)
'''
mail = Mail(app)


@app.route('/')
def index():
     msg = Message('Hello from the flask mail app!', sender= os.getenv("SECRET_SENDER"), recipients = [os.getenv("SECRET_SENDER")]) # temp-mail.org
     msg.body = "Testing text for the mail body"
     mail.send(msg)

     return "Message has been sent successfully!"


if __name__ == '__main__':
     app.run(debug=True)
     # app.run()
