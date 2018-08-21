def makeCodebook():
    decbook = {'5': 'a', '2': 'b', '#': 'd', '8': 'e', '1': 'f', '3': 'g', '4': 'h', '6': 'i', '0': 'l', '9': 'm', \
               '*': 'n', '%': 'o', '=': 'p', '(': 's', ';': 't', '?': 'u', '@': 'v', ':': 'y', '7': '',
               'D':'I'}

    encbook = {}
    for k in decbook:
        val = decbook[k]
        encbook[val] = k

    return encbook, decbook

def encrypt(msg, encbook):
    for c in msg:
        if c in encbook:
            msg = msg.replace(c, encbook[c])

    return msg

def decrypt(msg, decbook):
    for c in msg:
        if c in decbook:
            msg = msg.replace(c, decbook[c])

    return msg
'''
in map function
START 
'''
def addOne(value):
    return value + 1

myfunc = lambda value : value+1
'''
in map function
END 
'''

if __name__ == '__main__':
    '''
    #1. map 
    using function, lambda function
    START    
    '''
    # my_list = [1,2,3,4,5,6]
    # for d in map(myfunc,my_list):
    #     print(d, end=' ')
    # print(my_list)
    '''
    #1. map 
    END    
    '''

    '''
    #2. filter
    using lambda function
    START
    '''
    list_a = [1,2,3,4]
    list_b = [5,6,7,8]

    # result = list(map(lambda x,y:(x**2+y**2)**(1/2),list_a,list_b))
    # print(result)
    result = list(filter(lambda x : x%2==0, list_a))
    print(result)
    '''
    #2. filter
    using lambda function
    END
    '''

    '''
    #3. list converts to dictionary
    START
    '''
    words = ['zz','gg','dd','ww','dss']
    d_words = list(map(lambda x : {x:1}, words))
    print(d_words)
    '''
    #3. list converts to dictionary
    END
    '''

    '''
    #4. encrypt and decrypt
    START
    '''
    # plaintext = 'I love you with all my heart'
    #
    # encbook, decbook = makeCodebook()
    # ciphertext = encrypt(plaintext, encbook)
    # print(ciphertext)
    #
    # deciphertext =  decrypt(ciphertext, decbook)
    # print(deciphertext)
    # with open('plain.txt','r') as p_f:
    #     with open('encrypt.txt','w') as e_f:
    #         for line in p_f:
    #             e_f.write(encrypt(line, encbook))
    '''
    #4. encrypt and decrypt
    END
    '''
