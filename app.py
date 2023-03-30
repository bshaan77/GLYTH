from flask import Flask, render_template, request, redirect
import message
import helpers
import os
from newsscraper import get_articles




app = Flask(__name__)
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']='./static/jsonkey.json'


@app.route('/contact')
def result():
    # Call get_articles function to get the articles
    articles = get_articles(num_images=4)

    # Pass articles to render_template function
    return render_template('contact.html', articles=articles)

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
        print(phone_number)
        print(type(phone_number))
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
        if phone_number != "":
            message.send_message(phone_number, coords)
        return redirect('/contact')


@app.route('/contact')
def contact():
    # Get the articles
    result = get_articles(num_images=4)

    # Extract the information we need
    titles, urls, image_urls = [], [], []
    for article in result:
        titles.append(article['title'])
        urls.append(article['url'])
        image_urls.append(article['image_url'])

    # Create 12 variables
    title1, title2, title3, title4 = titles
    url1, url2, url3, url4 = urls
    image_url1, image_url2, image_url3, image_url4 = image_urls
    print(title1, url1, image_url1)

    return render_template('contact.html', title1=title1, title2=title2, title3=title3, title4=title4,
                                          url1=url1, url2=url2, url3=url3, url4=url4,
                                          image_url1=image_url1, image_url2=image_url2, image_url3=image_url3, image_url4=image_url4)



@app.route('/pricing') #by default is GET request
def leaderboard():
    return render_template('pricing.html')


if __name__ == '__main__':
    #./ngrok http 3000
    app.run(port=3000) #debug = True //in order to not run every time
