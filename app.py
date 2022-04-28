from flask import Flask
from flask_mail import Mail

app = Flask(__name__)


app.config['MAIL_SERVER']
app.config['MAIL_PORT']
app.config['MAIL_USE_TLS']
app.config['MAIL_USE_SSL']
app.config['MAIL_DEBUG']
app.config['MAIL_USERNAME']
app.config['MAIL_PASSWORD']
app.config['MAIL_DEFAULT_SENDER']
app.config['MAIL_MAX_EMAILS']
app.config['MAIL_SUPRESS_SEND']
app.config['MAIL_ASCII_ATTACHMENTS']


