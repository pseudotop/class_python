import hashlib, json
class TxIn():
    def __init__(self):
        self.hash = None # 사용할 UTXO가 포함된 해시
        self.n = 0 # 위 트랙잰션 중에서 몇 번째 UTXO인지
        self.address = '' # UTXO의 수신주소
        self.value = '' # UTXO의 잔액
        self.sign = '' # 서명
        self.pubk = '' # 사용자의 공개키

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True)

class TxOut():
    def __init__(self):
        self.to = '' # 받는 주소
        self.value = '' # 금액

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True)

class Transaction():
    def __init__(self):
        self.vin_sz = 0
        self.vout_sz = 0
        self.inputs = []
        self.outputs = []
        self.hash = None

    def can_spent(self):
        for input in self.inputs:
            pass

    def add_input(self,txin):
        self.inputs.append(json.loads(str(txin)))

    def add_output(self,txout):
        self.outputs.append(json.loads(str(txout)))

    def gen_hash(self):
        h = hashlib.sha256(str(self).encode()).hexdigest()
        self.hash = h

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True)

    def sign(self, priv):
        return priv

if __name__ == '__main__':
    pass
