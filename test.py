import requests

def containing_text(path, url, count):
    url = f'{url}/upload?top_word_count={count}'
    file = {'file': open(path, 'rb')}
    resp = requests.post(url=url, files=file) 
    print(resp.json())


url = 'http://127.0.0.1:80'
resp = requests.get(url=url) 
print(resp.json())

# how many words to take out of the top. [count]
count = 10
containing_text('documents/text1.txt', url, count)
containing_text('documents/text2.txt', url, count)
containing_text('documents/text3.txt', url, count)
containing_text('documents/text4.txt', url, count)
