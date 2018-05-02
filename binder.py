import re
import itertools

headers = [['Page1'],['Page2'],['Page3'],['Page4'],['Page No. 1'],['Page No. 2'],['Page No. 3'],[],[],[]]
footers = [[],[],[],[],[],[],[],['1/3'],['2/3'],['3/3'],['6'],['3']]

flag = []
flag_h = []
flag_rh = []
flag_lh = []
flag_f = []
flag_rf = []
flag_lf = []
header_score = []
footer_score = []

pattern1 = re.compile(r"\b(?:Page|page)(?:\s{0,}[a-zA-Z.,]*\s){0,3}[#]?\s*(\d{1,3}\b)")
pattern2 = re.compile(r"\b(\d{1,3})\s?(?:\/\s?\d{1,4})\b")
pattern3 = re.compile(r"\b(\d{1,3})\b")

for h in headers:
    flag_h.append(re.findall(pattern1,' '.join(h)))
    flag_rh.append(re.findall(pattern2,' '.join(h)))
    flag_lh.append(re.findall(pattern3, ' '.join(h)))
print(flag_h)
print(flag_rh)
print(flag_lh)
print('\n')

for f in footers:
    flag_f.append(re.findall(pattern1,' '.join(f)))
    flag_rf.append(re.findall(pattern2,' '.join(f)))
    flag_lf.append(re.findall(pattern3, ' '.join(f)))
print(flag_f)
print(flag_rf)
print(flag_lf)
print('\n')

for i3 in range (0,len(flag_h)-1):
    a = flag_h[i3]
    b = flag_h[i3+1]
    a1 = flag_rh[i3]
    b1 = flag_rh[i3+1]
    a2 = flag_lh[i3]
    b2 = flag_lh[i3+1]
    if a and b:
        if int(a[0]) == int(b[0])-1:
            print(a[0],b[0],"hI")
            header_score.append("I")
            continue
        else:
            print(a[0],b[0],"hB")
            header_score.append("B")
            continue
    if a1 and b1:
        a1 = map(int, a1)
        b1 = map(int, b1)
        x = [i for i in a1 if i + 1 in b1]
        if x:
            print(x,"hI")
            header_score.append("I")
            continue
        else:
            print(x,"hB")
            header_score.append("B")
            continue
    if a2 and b2:
        a1 = map(int, a1)
        b1 = map(int, b1)
        x = [i for i in a1 if i+1 in b1]
        if x:
            print(x[0],"hI")
            header_score.append("I")
            continue
        else:
            print(x[0],"hO")
            header_score.append("O")
            continue
    else:
        header_score.append([])
        print("hEmpty")

    i3 += 1
print('\n')

for i4 in range (0,len(flag_f)-1):
    a = flag_f[i4]
    b = flag_f[i4+1]
    a1 = flag_rf[i4]
    b1 = flag_rf[i4+1]
    a2 = flag_lf[i4]
    b2 = flag_lf[i4+1]
    if a and b:
        if int(a[0]) == int(b[0])-1:
            print(a[0],b[0],"fI")
            footer_score.append("I")
            continue
        else:
            print(a[0],b[0],"fB")
            footer_score.append("B")
            continue
    if a1 and b1:
        a1 = map(int, a1)
        b1 = map(int, b1)
        x = [i for i in a1 if i + 1 in b1]
        if x:
            print(x,"fI")
            footer_score.append("I")
            continue
        else:
            print(x,"fB")
            footer_score.append("B")
            continue
    if a2 and b2:
        a1 = map(int, a1)
        b1 = map(int, b1)
        x = [i for i in a1 if i+1 in b1]
        if x:
            print(x[0],"fI")
            footer_score.append("I")
            continue
        else:
            print(x[0],"fO")
            footer_score.append("O")
            continue
    else:
        footer_score.append([])
        print("fEmpty")

    i4+=1
print('\n')

print(header_score)
print(footer_score)

for a,b in itertools.izip_longest(header_score,footer_score):
    if a:
        flag.append(a)
    elif b:
        flag.append(b)
    else:
        flag.append([])

print(flag)
