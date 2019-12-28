import requests

text_to_speak = 'my little red orange'


url = 'https://translate.google.com/translate_tts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'
}
params = {
    'ie':'UTF-8',
    'q':text_to_speak,
    'tl':'en',
    'client':'gtx',
}

r = requests.get(url,params=params,headers=headers)
print(r.status_code)

with open('clip.mp3','wb') as f:
    f.write(r.content)
    
    
#?ie=UTF-8&q=3:40pm&tl=en&client=gtx