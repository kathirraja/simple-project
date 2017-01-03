from string import maketrans
r = []; c = []; ptlist=[]; etlist=[]
def make_unique_key(KEY):
    ks = ''; alp = KEY+'ABCDEFGHJKLMNOPQRSTUVWXYZ' 
    for l in alp:
        if l not in ks: ks+=l
    return ks
def fill_matrix(key):
    if 'i' and 'j' in key:
        return 'Renter key word'
    else:
        for i in range (0,25,5): r.append(key[i:i+5])
        for i in range(0,5):
            s = ''
            for j in range(0,5): s += r[j][i]
            c.append(s)
def make_s(s):
    s = s.upper().translate(maketrans('I','J')); s1=''
    for w in s:
        if w != ' ': s1+=w
    return s1
def splt(w):
    l = len(w); pt = ''; k = 0;
    while k+2<l:
        if w[k]==w[k+1]: pt += w[k]+'X'; k+=1
        else: pt+=w[k]+w[k+1]; k+=2
    if l-k == 1: pt+=w[k]+'X'
    elif l-k == 2:
        if w[k]!=w[k+1]: pt += w[k]+w[k+1]
        else: pt += w[k]+'X'+w[k+1]+'X'
    return pt
def make_plist(s):
    k = 0
    while k<len(s):
        ptlist.append(s[k]+s[k+1]); k+=2;
def row(ch):
    for i in range(5):
        if ch in r[i]: return i
def col(ch):
    for i in range(5):
        if ch in c[i]: return i
def encript():
    es = ''
    for w in ptlist:
        i1 = row(w[0]); i2 = row(w[1]); j1 = col(w[0]); j2 = col(w[1])
        if i1 == i2:
            j1 += 1; j2 += 1
            if(j1>=5): j1 -= 5
            if(j2>=5): j2 -= 5
            es +=r[i1][j1]+r[i1][j2]
            etlist.append(r[i1][j1]+r[i1][j2])
        elif j1 == j2:
            i1+=1; i2+=1
            if(i1>=5): i1 -= 5
            if(i2>=5): i2 -= 5
            es +=r[i1][j1]+r[i2][j1]
            etlist.append(r[i1][j1]+r[i2][j1])
        else:
            es +=r[i1][j2]+r[i2][j1]
            etlist.append(r[i1][j2]+r[i2][j1])
    return es

fill_matrix(make_unique_key(make_s(raw_input('Enter key String : '))))
make_plist(splt(make_s(raw_input('Enter plain text : '))))
for i in range(5):
    print r[i]
print ptlist
print etlist
print encript()
