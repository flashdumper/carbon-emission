from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    # return render_template('index2.html', tests=[1,2], tests_count=1, session=1)
    # message = "Image Route"
    # return render_template('image.html', message=message)
    return render_template('materials.html')

@app.route("/profile", methods=['GET'])
def profile():
    # return render_template('index2.html', tests=[1,2], tests_count=1, session=1)
    # message = "Image Route"
    # return render_template('image.html', message=message)
    return render_template('profile.html')



if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0',port=5000,debug=True)

