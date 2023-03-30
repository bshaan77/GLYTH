import requests
from PIL import Image

# Key
apiKey = 'e580d034e43c4e79b6a91561e66c0f61'

# API endpoint
apiEndpoint = f'https://newsapi.org/v2/everything?q=deforestation&apiKey={apiKey}&pageSize=10'

# Send GET request to API
response = requests.get(apiEndpoint)

data = response.json()


def get_articles(num_images=4):
    printed_urls = set()
    result = []
    num_images_printed = 0
    for article in data['articles']:
        if article['url'] not in printed_urls and 'deforestation' in article['title'].lower() and article['urlToImage'] and num_images_printed < num_images:
            # Append article information to result
            result.append({
                "title": article['title'],
                "url": article['url'],
                "image_url": article['urlToImage']
            })

            #resize image
            image = Image.open(requests.get(article['urlToImage'], stream=True).raw)
            image = image.resize((300, 300))
            image.show()
            
            num_images_printed += 1
            printed_urls.add(article['url'])
            
            if num_images_printed == num_images:
                break
                
            for replacement_article in data['articles']:
                if replacement_article['title'].lower() == article['title'].lower() and replacement_article['url'] not in printed_urls:
                    break
                
                if replacement_article['urlToImage'] and replacement_article['url'] not in printed_urls and 'deforestation' in replacement_article['title'].lower() and num_images_printed < num_images:
                    # Append article information to result
                    result.append({
                        "title": replacement_article['title'],
                        "url": replacement_article['url'],
                        "image_url": replacement_article['urlToImage']
                    })

                    image = Image.open(requests.get(replacement_article['urlToImage'], stream=True).raw)
                    image = image.resize((300, 300))
                    image.show()
                    
                    num_images_printed += 1
                    printed_urls.add(replacement_article['url'])
                    
                    if num_images_printed == num_images:
                        break
                    
            if num_images_printed == num_images:
                break
                
    return result

result = get_articles(num_images=4)
titles = []
urls = []
image_urls = []

for article in result:
    title = article['title']
    url = article['url']
    image_url = article['image_url']

    titles.append(title)
    urls.append(url)
    image_urls.append(image_url)

    
