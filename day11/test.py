from bitcoin import *

priv = sha256('turing')
pubk = privtopub(priv)
addr = pubtoaddr(pubk)
print(addr)