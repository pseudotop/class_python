from bs4 import BeautifulSoup
import urllib.request as req
import re
import urllib.parse as parse
import io
from eunjeon import Mecab
import tkinter as tk
import matplotlib as plt
plt.use('TkAgg')
from matplotlib import style
style.use('ggplot')

import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation

import sys

class Search:
    gurl = 'http://www.zdnet.co.kr'
    def __init__(self):
        self.gheader = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
        self.visited = {}
        self.dict_text = {}
        self.sum_search = 0
        try:
            self.MAX_DEPTH = int(input("DFS depth: "))
        except:
            self.MAX_DEPTH = 1

        sum_search=self.go(count_search=0)
        print(self.dict_text)
        file = io.open("cr_result_1.txt", "w", encoding='utf8')

        # sort using a lambda expression
        sorted_dict_text = sorted(self.dict_text, key=lambda x: self.dict_text[x], reverse=True)
        file.write("="*50+"\n")
        file.write("Depth:" + str(self.MAX_DEPTH) + "\n")
        file.write("Count_Searching_Page:" + str(sum_search) + "\n")
        file.write("Total_Words:" + str(sum(self.dict_text.values())) + "\n")
        file.write("="*50+"\n")
        for k in sorted_dict_text:
            item = "{} : {}".format(k, self.dict_text[k])
            print(item)
            file.write(item + '\n')

        file.close()

    def go(self,url=gurl, depth=0, count_search=0):
        print(url, 'depth:', depth)
        reurl = req.Request(
            url,
            data=None,
            headers=self.gheader
        )
        f = req.urlopen(reurl)
        text = f.read().decode('utf-8')
        soup = BeautifulSoup(text, 'html.parser')
        refs = soup.find_all(href=re.compile("news/news_view"))
        try:
            tagger = Mecab()
            res = soup.select_one('div.sub_view_cont')
            ptext = res.get_text()
            lltext = tagger.nouns(ptext)
            print(tagger.nouns(ptext))
            for i in lltext:
                try:
                    self.dict_text[i] += 1
                except:
                    self.dict_text[i] = 1

            # print(ptext)
            # ltext = ptext.split()
            # for i, j in enumerate(ltext):
            #     if j[-1] in ['은', '는', '이', '가', '을', '를', '의']:
            #         ltext[i] = j[:-1]
            #         try:
            #             self.dict_text[ltext[i]] += 1
            #         except:
            #             self.dict_text[ltext[i]] = 1
            # print(ltext)
        except AttributeError:
            pass
        if (depth >= self.MAX_DEPTH): return count_search
        for r in refs:
            suburl = r['href']
            result = parse.urlparse(suburl)
            result2 = parse.parse_qs(result.query)
            theval = False
            try:
                theval = self.visited[result2['artice_id'][0]]
            except KeyError:
                pass
            if not theval:
                self.visited[result2['artice_id'][0]] = True
                if 'http' in suburl:
                    count_search += self.go(suburl, depth + 1)
                else:
                    count_search += self.go(self.gurl + suburl, depth + 1)
                count_search += 1
        return count_search

class UI():
    def __init__(self, *args, **kwargs):
        self.window = tk.Tk()
        self.window.wm_title("Text Mining on Web")
        self.f = Figure(figsize=(5, 4), dpi=100)
        self.plt = self.f.add_subplot(111)
        # self.plt.set_autoscale_on(True)
        # self.plt.plot([0], [0])
        # self.plt.set_title('Tk embedding')
        # self.plt.set_xlabel('X axis label')
        # self.plt.set_ylabel('Y label')

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(self.f, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.running = False
        startButton = tk.Button(self.window, text="시작",bg="yellow",command=self.start)
        startButton.pack(side=tk.BOTTOM)
        stopButton = tk.Button(self.window, text="중지",bg="yellow",command=self.stop)
        stopButton.pack(side=tk.BOTTOM)
        exitButton = tk.Button(self.window, text='나가기', command=sys.exit)
        exitButton.pack(side=tk.BOTTOM)

        self.startTimer()

    def update_line(self, new_key, new_value):
        self.xarr = []
        self.yarr = []
        self.xarr = np.append(self.xarr, new_key)
        self.yarr = np.append(self.yarr, new_value)
        self.plt.relim()
        self.plt.autoscale_view()
        self.plt.clear()
        self.plt.plot(self.xarr, self.yarr)

    def startTimer(self):
        if(self.running):
            for k in self.search.dict_text:
                self.update_line(k, self.search.dict_text[k])
        self.window.after(10, self.startTimer)

    def start(self):
        self.running = True
        self.search = Search()

    def stop(self):
        self.running = False

gui = UI()
gui.window.mainloop()
