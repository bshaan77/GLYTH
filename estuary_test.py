import requests


url = "https://api.estuary.tech/content/add"


payload={}
files=[
  ('data',('file',open('result.png','rb'),'application/octet-stream'))
]
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer EST78a8d35e-2d1f-42e5-8207-c784e49b4de0ARY'
}


response = requests.request("POST", url, headers=headers, data=payload, files=files)


print(response.text)

#ON WEBISTE
### POST Location
### GET retrival_url

#HERE
### GET Location
### POST retrival_url (can be then GET in the webapp to display the image)

