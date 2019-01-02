from bitcoin import *
from transaction2 import *
from block import Block
from flask import Flask, render_template, request, jsonify
import webbrowser
import json
import pprint
from multiprocessing import Value

from multiprocessing import Process
import threading

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def gen_address(string):
    priv = sha256(string)
    pubk = privtopub(priv)
    addr = pubtoaddr(pubk)
    return addr, priv

class Blockchain():
    def __init__(self):
        self.chain = []
        self.genesis_block = Block(0)
        self.genesis_block.bits = 4 # 초기 난이도
        self.genesis_block.gen_hash()
        self.chain.append(self.genesis_block)
        self.curr_reward = 50

    def get_latest_block(self):
        return self.chain[len(self.chain)-1]
    def add_block(self,new_block):
        new_block.prev_hash = self.get_latest_block().hash
        new_block.hash = new_block.gen_hash()
        tx = Transaction()
        txout = TxOut()
        txout.to = gen_address(names[0])[0]
        txout.value = self.curr_reward

        tx.add_output(txout)
        print("rewarding miner : " , txout)
        new_block.add_transaction(tx)

        print(" tx : ", tx)

        self.chain.append(new_block)

    def __str__(self):
        blocklist = []
        for block in self.chain:
            blocklist.append(json.loads(str(block)))
        print(blocklist)
        return str(blocklist)

class ChromeBrowser():
    def __init__(self, chrome_path, url):
        self.chrome_path = chrome_path
        self.url = url
        self.chrome = webbrowser.get(self.chrome_path)
        self.chrome.open(self.url)
    def __del__(self):
        shutdown_server()

names = ['a','b','c','d']
altCoin = Blockchain()
idx = 1

# altCoin.add_block(Block(1))
# altCoin.add_block(Block(2))

url = 'localhost'
# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

counter = Value('i', 0)
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
@app.route('/')
def index():
    print('요청이 들어옵니까')
    return render_template('index.html', result={'a':20, 'b':30})

@app.route('/hello')
def hello():
    print(altCoin)
    return jsonify(str(altCoin))

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


def getUnspentUTXOs(name):
    list = []
    chain = altCoin.chain  # Blockchain['getChaina
    priv = sha256(name)
    pubk = privtopub(priv)
    addr = pubtoaddr(pubk)

    for block in chain:
        for tx in block.transactions:
            for elm in tx.input:
                if elm.address == addr:
                    list0 = [x for x in list if not (x == elm.hash and x.n == elm.n)]
            for idx, elm in enumerate(tx.outputs):
                if elm.to == addr:
                    dict0 = {}
                    dict0.txhash = tx.hash
                    dict0.n = idx
                    dict0.value = elm.value
                    list.append(dict0)

    return list


@app.route('/getutxos')
def get():
    a = {}
    for name in names:
        a[name] = getUnspentUTXOs(name)
    return render_template('index.html', result=a)


'''
result = {
    'alice': [
        {
            txhash = egaw2332tg3ga3t3
            n = 2
            value = 100
        },
        {

        },
    ],
    'bob' : [

    ]
}
'''


@app.route('/tx')
def tx():
    curr_block = altCoin.get_latest_block()
    from_ = request.args.get('from')
    val = int(request.args.get('value'))
    to = request.args.get('to')

    list = getUnspentUTXOs(from_)

    sum = 0
    for idx, elm in enumerate(list):
        sum += elm.value
        if sum >= val:
            list = list[:idx + 1]
            break;

    tx = Transaction()

    for elm in list:
        txin = TxIn()
        tx.add_input(txin)

    txout = TxOut()
    txout.to = to
    txout.value = val
    tx.add_output(txout)

    if sum > val:
        txout = TxOut()
        txout.to = gen_address(from_)[0]
        txout.value = sum - val
        tx.add_output(txout)

    tx.sign(gen_address(from_)[1])

    curr_block.add_transaction(tx)
    return get()

ismining = False
@app.route('/mine')
def is_mining():
    global ismining
    if ismining:
        return 'true'
    else:
        ismining = True
        altCoin.add_block(Block(altCoin.get_latest_block().index+1))
        ismining = False
        return 'false'

chrome = ChromeBrowser(chrome_path, url+'/hello')
app.run(url,'80')

