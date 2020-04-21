import requests

# NOT WORKING --- NO ACCESS TO GOOGLE.

text = 'Where is my key?'

url = 'https://translate.google.com/translate_a/single'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'
}
params = {
    #'ie':'UTF-8',
    'tl':'pl',
    'sl':'en',
    'hl':'en',
    'client':'webapp',
    'otf':1,
    'ssel':3,
    'tsel':6,
    'xid':1791807,
    'kc':3,
    'tk':869111.783626,
    'q':text,
}

r = requests.get(url,params=params,headers=headers)
print(r.status_code)

with open('translated.json','wb') as f:
    f.write(r.content)

#https://translate.google.com/translate_a/single?client=webapp&sl=en&tl=pl&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=1&ssel=3&tsel=6&xid=1791807&kc=3&tk=869111.783626&q=cat