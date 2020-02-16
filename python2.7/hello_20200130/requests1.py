import requests

r = requests.get('http://www.google.com', timeout=(5,15))
print(r.text, r.status_code)

custom_cookie = {'cookie_name': 'cookie_value'}
r = requests.get('http://example.com/cookies', cookies=custom_cookie)

custom_header = {'user-agent': 'customUserAgent'}
r = requests.get('https://samplesite.org', headers=custom_header)

r = requests.get('https://example.com/1280.jgp', stream=True)
downloaded_file = open("1280.jpg", "wb")
for chunk in r.iter_content(chunk_size=256):
    if chunk: downloaded_file.write(chunk)

r = requests.get("http://exampleurl.com", stream=True)
print(r.raw)