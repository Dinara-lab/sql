import numpy as np


alphabet = "abcdefghijklmnopqrstuvwxyz1_34".lower()
text_enc = []
while True:
    v = input("""what you want to do:
    1.encrypt
    2.decrypt
    3.exit\n""")
    enc = []
    text_decr = []
    def get_pos(k,l):
        for i in range(6):
            for j in range(5):
                if matrix[i][j] == k:
                    x,y = i,j
                if matrix[i][j] == l:
                    x1,y1 = i,j
        m = [y,y1,x,x1]
        return m
    #encrypt
    if int(v) == 1:
        key = input("key to encrypt: ").lower()
        text = input("text to encypt: ").lower()
        for i in key:
            if i not in alphabet:
                key = key.replace(i,'')
        key = ''.join(sorted(set(key), key = key.index))
        for i in key:
            if i in alphabet:
                alphabet = alphabet.replace(i,'',1)
        alphabet = key + alphabet
        matrix = np.array(list(alphabet)).reshape(6,5)
        if len(text) % 2 ==1:
            text = text + 'z'
        for k in range(0,len(text),2):
            a = get_pos(text[k],text[k+1])
            if a[2] == a[3]:
                for i in range(2):
                    
                    enc.append(matrix[a[2]][(a[i] + 1) % 5])
            
            elif a[0] == a[1]:
                for i in range(2,4):
                    
                    enc.append(matrix[(a[i] +1) % 6][a[0]])
            else:
                enc.append(matrix[a[2]][a[1]])
                enc.append(matrix[a[3]][a[0]])
        text_enc = ''.join(str(i) for i in enc)
        print("encrypted text is: ",text_enc)
    #decrypt
    elif int(v) == 2:
        print("decrypt is not ready!!!")
    elif int(v) == 3:
        break
    else:
        print("select 1 or 2 or 3!")

