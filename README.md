# Flask Mail App

A simple flask mail server app for sending emails using the [flask-mail](https://pythonhosted.org/Flask-Mail/) extension.

## Usage

* Clone or download the repo files
* Navigate to `app.py` and replace the values based on your own email:
     * app.config['MAIL_USERNAME']
     * app.config['MAIL_PASSWORD']
     * sender
     * recipients
* Based on your email provider you might also need to change accordingly the values for:
     * app.config['MAIL_SERVER']
     * app.config['MAIL_PORT']     

## License

* [MIT License](https://opensource.org/licenses/MIT)
