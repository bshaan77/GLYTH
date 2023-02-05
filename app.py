from flask import Flask,render_template, request, redirect
import helpers
import os

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        coords = request.form["coords"]
        coordinates = coords.split(',')
        try:
            os.remove('static/AfterImage.png')
            os.remove('static/BeforeImage.png')
            os.remove('static/outputAfter.png')
            os.remove('static/outputBefore.png')
            os.remove('static/result.png')
        except:
            print('hello')
        helpers.getBeforeAndAfterImages(coordinates)
        return redirect('/result')
        
@app.route('/result') #by default is GET request
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run() #debug = True in order to not run every time