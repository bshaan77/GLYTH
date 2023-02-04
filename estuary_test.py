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


response_txt = response.text
print(response_txt)
url_s = (response_txt.find('estuary_retrieval_url'))+ 24
url_e = (response_txt.find('estuaryId')) - 3 - url_s
print(url_s,url_e)
print("hi")
print(response_txt[url_s:url_s+url_e:1])


#ON WEBISTE
### POST Location
### GET retrival_url

#HERE
### GET Location
### POST retrival_url (can be then GET in the webapp to display the image)

