# Flask Mail App

A simple flask mail server app for sending emails using the [flask-mail](https://pythonhosted.org/Flask-Mail/) extension.

## Usage

* Clone or download the repo files
* Install pipenv: `pip install pipenv`
* Navigate to the root project path and create your virtual environment: `pipenv shell`
* Install the required packages: `pipenv install`
* Navigate to `app.py` and replace the values based on your own email:
     * app.config['MAIL_USERNAME']
     * app.config['MAIL_PASSWORD']
     * sender
     * recipients
* Based on your email provider you might also need to change accordingly the values for:
     * app.config['MAIL_SERVER']
     * app.config['MAIL_PORT']   
* Run `python app.py` and navigate to localhost:5000
* If you've followed all steps correctly you should then view a message "*Hello from the flask mail app!*" on localhost:5000, and the email *Testing text for the mail body* on your email inbox.

## License

* [MIT License](https://opensource.org/licenses/MIT)
