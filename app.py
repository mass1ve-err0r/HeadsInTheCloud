from flask import Flask, render_template
from Blueprints.Browser.route import BrowserBP


app = Flask(__name__)
app.secret_key = b'YOUR_SUPER_SECRET_KEY'
app.register_blueprint(BrowserBP)


@app.route('/')
def index():
    return render_template('Homepage.html')


@app.route('/contact')
def contactme():
    return render_template('Contact.html')


if __name__ == '__main__':
    app.run(debug=True)
