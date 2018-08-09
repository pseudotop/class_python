import urllib.request as req
url = 'http://www.naver.com'
# req.urlretrieve(url,'naver.html')
data = req.urlopen(url).read()
# print(data)
text = data.decode('utf-8')
print(text)