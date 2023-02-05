from flask import Flask, render_template, request, redirect
import helpers
import os
import requests
from twilio.rest import Client

#twilio setup -- to be converted to env variables
account_sid = "AC1a2e909926f462233a69d2ec20f1a229"
auth_token = "0d3e4531336506891caf8d26aa9781f9"

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "GET":
        return render_template('index.html')
    

@app.route('/features', methods = ["GET", "POST"])
def features():
    if request.method == "GET":
        return render_template('features.html')
    
    else:
        phone_number = request.form["phone_number"]
        coords = request.form["coords"]
        coordinates = coords.split(',')
        try:
            os.remove('static/AfterImage.png')
            os.remove('static/BeforeImage.png')
            os.remove('static/outputAfter.png')
            os.remove('static/outputBefore.png')
            os.remove('static/result.png')
        except:
            pass
        helpers.getBeforeAndAfterImages(coordinates)
        return redirect('/contact')


#estuary set up
url = "https://api.estuary.tech/content/add"

payload={}
files=[
  ('data',('file',open('static/BeforeImage.png','rb'),'application/octet-stream'))
]
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer EST78a8d35e-2d1f-42e5-8207-c784e49b4de0ARY'
}
response = requests.request("POST", url, headers=headers, data=payload, files=files)
response_txt = response.text
url_s = (response_txt.find('estuary_retrieval_url'))+ 24
url_e = (response_txt.find('estuaryId')) - 3 - url_s
BeforeURL= (response_txt[url_s:url_s+url_e:1])

payload={}
files=[
  ('data',('file',open('static/result.png','rb'),'application/octet-stream'))
]
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer EST78a8d35e-2d1f-42e5-8207-c784e49b4de0ARY'
}
response = requests.request("POST", url, headers=headers, data=payload, files=files)
response_txt = response.text
url_s = (response_txt.find('estuary_retrieval_url'))+ 24
url_e = (response_txt.find('estuaryId')) - 3 - url_s
AfterURL= (response_txt[url_s:url_s+url_e:1])


#Send Message
client = Client(account_sid, auth_token)
client.messages.create(
    to=phone_number,
    from_="+19136758450",
    body=(f'You can view the before and after satelite images for deforestation for {coords} coordinates here: /nBefore: {BeforeURL}/nAfter: {AfterURL}')
    )
        
@app.route('/contact') #by default is GET request
def result():
    return render_template('contact.html')

@app.route('/pricing') #by default is GET request
def leaderboard():
    return render_template('pricing.html')


if __name__ == '__main__':
    #./ngrok http 3000
    app.run(port=3000) #debug = True in order to not run every time
