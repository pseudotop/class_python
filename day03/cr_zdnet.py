from bs4 import BeautifulSoup
import urllib.request as req
import re
import urllib.parse as parse
import io

try:
    MAX_DEPTH = int(input("DFS depth: "))
except:
    MAX_DEPTH = 1

gheader = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}
gurl = 'http://www.zdnet.co.kr'
dict_text = {}
visited = {}
sum_search = 0

def go(url=gurl, depth=0, count_search=0):
    print(url, 'depth:', depth)
    reurl = req.Request(
        url,
        data=None,
        headers=gheader
    )
    f = req.urlopen(reurl)
    text = f.read().decode('utf-8')
    soup = BeautifulSoup(text, 'html.parser')
    refs = soup.find_all(href=re.compile("news/news_view"))
    try:
        res = soup.select_one('div.sub_view_cont')
        ptext = res.get_text()
        # print(ptext)
        ltext = ptext.split()
        for i, j in enumerate(ltext):
            if j[-1] in ['은', '는', '이', '가', '을', '를', '의']:
                ltext[i] = j[:-1]
                try:
                    dict_text[ltext[i]] += 1
                except:
                    dict_text[ltext[i]] = 1
        print(ltext)
    except AttributeError:
        pass
    if (depth >= MAX_DEPTH): return count_search
    for r in refs:
        suburl = r['href']
        result = parse.urlparse(suburl)
        result1 = result.query
        result2 = parse.parse_qs(result.query)
        theval = False
        try:
            theval = visited[result2['artice_id'][0]]
        except KeyError:
            pass
        if not theval:
            visited[result2['artice_id'][0]] = True
            if 'http' in suburl:
                count_search += go(suburl, depth + 1)
            else:
                count_search += go(gurl + suburl, depth + 1)
            # print(result1)
            # print(result2)
            count_search += 1
    return count_search


sum_search=go(count_search=0)
print(dict_text)
file = io.open("cr_result.txt", "w", encoding='utf8')
# sort using a lambda expression
sorted_dict_text = sorted(dict_text, key=lambda x: dict_text[x], reverse=True)
file.write("="*50+"\n")
file.write("Depth:" + str(MAX_DEPTH) + "\n")
file.write("Count_Searching_Page:" + str(sum_search) + "\n")
file.write("Total_Words:" + str(sum(dict_text.values())) + "\n")
file.write("="*50+"\n")
for k in sorted_dict_text:
    item = "{} : {}".format(k, dict_text[k])
    print(item)
    file.write(item + '\n')

file.close()
