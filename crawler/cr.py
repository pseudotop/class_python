from bs4 import BeautifulSoup
import urllib.request as req
import re
import urllib.parse as parse
import io
from eunjeon import Mecab
import tkinter as tk
from tkinter import ttk
import matplotlib as plt
plt.use('TkAgg')
plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['figure.figsize'] = (14,4)
plt.rcParams.update({'figure.autolayout':True})
from matplotlib import style
style.use('ggplot')

import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import threading

import sys

class StoppableThread(threading.Thread):
    """stop() 매써드를 포함한 Thread 클래스.
    쓰레드 자체에서 정기적으로 stopped() 상태를 체크해야합니다."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

class Search(threading.Thread):
    gurl = 'http://www.zdnet.co.kr'
    def __init__(self, max_depth=0):
        threading.Thread.__init__(self)
        self.gheader = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
        self.visited = {}
        self.dict_text = {}
        self.sum_search = 0
        self.MAX_DEPTH = max_depth

    def setMaxdepth(self,max_depth):
        self.MAX_DEPTH = max_depth

    def run(self):
        self.sum_search=self.go(count_search=0)
        print(self.sum_search)

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
    def saveFile(self,*args):
        print(self.dict_text)
        jsonlist = {
            'dict_text':self.dict_text,
            'sum_search':self.sum_search,
            'MAX_DEPTH':self.MAX_DEPTH
        }
        if(len(args)==0): args = ('txt')
        FileIO(*args,jsonlist)

class FileIO:
    def __init__(self, *args, **kwargs):
        self.writeFile(*args,**kwargs)

    def writeFile(self,*args,**kwargs):
        if len(args) != 1:
            '''
            please input 1 argments
            '''
            return
        if args[0] == 'json':
            pass
        if args[0] == 'txt':
            file = io.open("cr_result.txt", "w", encoding='utf8')

            # sort using a lambda expression
            sorted_dict_text = sorted(kwargs['dict_text'], key=lambda x: kwargs['dict_text'][x], reverse=True)
            file.write("="*50+"\n")
            file.write("Depth:" + str(kwargs['MAX_DEPTH']) + "\n")
            file.write("Count_Searching_Page:" + str(kwargs['sum_search']) + "\n")
            file.write("Total_Words:" + str(sum(kwargs['dict_text'].values())) + "\n")
            file.write("="*50+"\n")
            for k in sorted_dict_text:
                item = "{} : {}".format(k, kwargs['dict_text'][k])
                print(item)
                file.write(item + '\n')

            file.close()

class UI:
    def __init__(self, *args, **kwargs):
        self.stopThread = StoppableThread()
        self.search = Search()
        self.window = tk.Tk()
        self.window.wm_title("Text Mining on Web")
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.plt = self.fig.add_subplot(111)
        self.xarr = []
        self.yarr = []
        # self.plt.set_autoscale_on(True)
        # self.plt.plot([0], [0])
        # self.plt.set_title('Tk embedding')
        # self.plt.set_xlabel('X axis label')
        # self.plt.set_ylabel('Y label')

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=0, columnspan=5, ipadx=100,ipady=100)

        # canvas._tkcanvas.grid(column=0, row=0, columnspan=3, padx=3, pady=3)

        self.running = False
        inputLabel = ttk.Label(self.window, text="Searching Depth")
        inputLabel.grid(column=0,row=1)
        self.var = tk.StringVar()
        inputText = ttk.Entry(self.window, width=15, textvariable=self.var)
        inputText.grid(column=1,row=1,columnspan=2, sticky=tk.W)

        startButton = ttk.Button(self.window, text="시작",command=self.start)
        startButton.grid(column=0,row=2)
        stopButton = ttk.Button(self.window, text="중지",command=self.stop)
        stopButton.grid(column=1,row=2)
        saveButton = ttk.Button(self.window, text="Save File",command=self.save)
        saveButton.grid(column=0,row=3)
        loadButton = ttk.Button(self.window, text="Load File",command=self.load)
        loadButton.grid(column=1,row=3)
        exitButton = ttk.Button(self.window, text='나가기', command=sys.exit)
        exitButton.grid(column=4,row=3)

        # self.startTimer()
        self.anim = animation.FuncAnimation(self.fig,self.update_line,interval=1000)

    def update_line(self,i):
        if(self.stopThread.stopped()):
            self.stopThread.stop()
            self.search.join()
        self.xarr.clear()
        self.yarr.clear()
        dic = sorted(self.search.dict_text, key=lambda x: self.search.dict_text[x], reverse=True)
        #for k in list(self.search.dict_text): # To avoid runtime error
        cnt = 0
        for k in list(dic): # To avoid runtime error
            if len(k)==1: continue
            if cnt >= 10:
                break
            self.xarr.append(k)
            self.yarr.append(self.search.dict_text[k])
            cnt+=1

        N = np.arange(1,cnt+1)
        nparr = np.array(self.yarr)
        # print(N)
        # print(nparr)
        self.plt.clear()
        self.plt.relim()
        self.plt.autoscale_view()
        if len(self.xarr) > 0 :
            self.plt.set_xticks(N)
            self.plt.set_xlim([0,cnt+1])

        self.plt.xaxis.set_major_locator(plt.ticker.MaxNLocator(cnt+1))
        self.plt.bar(N, nparr, align='center',tick_label=self.xarr)
        for tick in self.plt.get_xticklabels():
            tick.set_rotation(45)
        self.plt.set_xlabel('nouns')
        self.plt.set_ylabel('Counts')
        self.plt.set_title('Text Mining')
        self.plt.axhline()
        # self.plt.invert_xaxis()

    def startTimer(self):
        # if(self.running):
        #     for k in list(self.search.dict_text): # To avoid runtime error
        #         self.update_line(k, self.search.dict_text[k])
        # self.window.after(10, self.startTimer)
        pass

    def start(self):
        print(len(self.var.get()))
        if len(self.var.get())!=0:
            self.running = True
            self.search.setMaxdepth(int(self.var.get()))
            self.search.daemon = True
            self.search.start()

    def stop(self):
        self.running = False
        self.stopThread.stop()
        self.search.join()
        # self.search.stop()

    def save(self):
        self.search.saveFile('txt')
        pass

    def load(self):
        pass
gui = UI()
gui.window.mainloop()
