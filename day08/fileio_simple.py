with open('phones.txt','r',encoding='cp949') as f_in:
    with open('phones_copy2.txt','w',encoding='utf-8') as f_out:
        for i in f_in.readlines():
            f_out.write(i)