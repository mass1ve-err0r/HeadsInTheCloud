from flask import Flask, render_template
from Blueprints.Browser.route import BrowserBP


app = Flask(__name__)
app.secret_key = b'YOUR_SUPER_SECRET_KEY'
app.register_blueprint(BrowserBP)


@app.route('/')
def hello_world():
    return render_template('Homepage.html')


if __name__ == '__main__':
    app.run(debug=True)


'''
@app.route('/test')
def tests():
    x = 0
    for root, framework, files in os.walk('SDKs/iOS124/SpringBoard'):
        for entry in files:
            print("\"" + entry + "\",")
    print(x)
    return 'OK !'
'''
