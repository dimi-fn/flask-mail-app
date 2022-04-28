from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['DEBUG'] = True
# app.config['MAIL_DEBUG'] = True

app.config['TESTING'] = False
# app.config['MAIL_SUPRESS_SEND'] = False # when testing don't send mails

# change this based on the email domain 
app.config['MAIL_SERVER'] = "smtp.gmail.com"

# depends on the email client provider
app.config['MAIL_PORT'] = 465 # change this based on the email client, gmail has 465

# for security and encryption
app.config['MAIL_USE_TLS'] = False

# secure Sockets Layer
app.config['MAIL_USE_SSL'] = True

app.config['MAIL_USERNAME'] = ''

app.config['MAIL_PASSWORD'] = ''

# the email comes from..
# if none then use the default sender
app.config['MAIL_DEFAULT_SENDER'] = '' # same as mail_username

# restrict the number of emails sent
app.config['MAIL_MAX_EMAILS'] = None

# convert attached filenames from unicode to ascii
app.config['MAIL_ASCII_ATTACHMENTS'] = False


# initialize 
'''
mail = Mail()
mail.init_app(app)
'''
mail = Mail(app)


@app.route('/')
def index():
     msg = Message('Hello from the flask mail app', recipients = ['bafigiv355@ovout.com'])
     mail.send(msg)

if __name__ == '__main__':
     app.run()

