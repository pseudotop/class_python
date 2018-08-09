import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as parse

url = 'https://search.shopping.naver.com/search/all.nhn'
params = {
    'query' : '아이스크림'
}
#아이스크림 -> %EC%95%84%EC%9D%B4%EC%8A%A4%ED%81%AC%EB%A6%BC

query_string = parse.urlencode(params)
text=req.urlopen(url + "?" +query_string).read().decode('utf-8')
#print(text)

soup = BeautifulSoup(text,'html.parser')
goods = soup.select('ul.goods_list li')
name = goods[0].select_one('div.info a')
print(name.get_text().lstrip())

img = goods[0].select_one('div.img_area img')
print(img['src'])

price = goods[0].select_one('span.num._price_reload')
print(price.text)
#print(price[0].get_text())

mall_list = goods[0].select_one('ul.mall_list')
if(mall_list == None) :
    mall_name = goods[0].select_one('div.info_mall a.mall_more')
    print(mall_name['title'])
else :
    mall = mall_list.select_one('li')
    mall_name = mall.select_one('span.mall_name')
    print(mall_name.text)
# for good in goods:
#     print(type(good.select('a.img')))
#     print(good.select('a.img'))
