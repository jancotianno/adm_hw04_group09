# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:19:55 2018

@author: Betglad
"""

def c_mul(a, b):
    return eval(hex((int(a) * b) & 0xFFFFFFFF)[:-1])

def same(s1, s2):
    if len(s1) != len(s2):
        res = False
        return res
    else:
        if sorted(s1) == sorted(s2): res = True
        else: res = False
    return res

def toAscii(s):
    #res = ""
    value = ord(s[0]) << 7
    for c in s:
        #res += str(ord(c))
        value = c_mul(1000003, value) ^ ord(c)
    return value

diz_ascii = {}
n_lines = 110000000
duplicates = 10000000
slots = n_lines / duplicates
#f = pd.read_csv("C:\\Users\\Betglad\\Desktop\\adm_hw04\\passwords2.txt", delimiter="\n")

path = 'C:\\Users\\Betglad\\Desktop\\adm_hw04\\passwords2.txt'
with open(path, 'r', encoding='utf-8') as f:
    #head = [next(f) for x in range(50)]
    for s in range(150):
        lst = []
        asc = toAscii(next(f))
        lst.append(asc)
        lst.append(int(asc % slots))        
        diz_ascii[next(f)] = lst
        
diz_slots = {}

for i in range(int(slots)):
    diz_slots[i] = [k for k, v in diz_ascii.items() if v[1] == i]
    

for k, v in diz_slots.items():
    print(k, v)


#num_lines = sum(1 for line in open('C:\\Users\\Betglad\\Desktop\\adm_hw04\\passwords2.txt', 'r', encoding='utf-8'))
#[print(l) for l in head]
#print(num_lines)    
#print(len(head))

uguali = []
diverse = [] 
n = 1 

s1 = "6<qr=lgh&$uyG5V>C:YT"
print(toAscii(s1))
"""print(toAscii(s1) % slots)
s2 = "!bc;3,rl5m1+N:BRT%px"
print(toAscii(s2) % slots)
s3 = "l2*$Sr4T<3QaGfF(hK1Z"
print(toAscii(s3) % slots)
s4 = "@gfjLKq5!C8dbxHFEw>+"
print(toAscii(s4) % slots)
#lst = [s1, s2, s3, s4]

print(same(s2, s3))"""

"""for st1 in lst:
    for st2 in lst[1:]:
        if same(st1, st2):
            uguali.append(st1)
            uguali.append(st2)
        else: diverse.append(st2)"""
    
"""for s1 in head:
    for s2 in head[n:]:
        if same(s1, s2):
            uguali.append(s1)
            #uguali.append(s2)
            #n+=1
        else:
            diverse.append(s1)
            #diverse.append(s2)
            #n+=1"""

#print(set(diverse))
    
#print(num_lines)
#for s in diverse:
#    print(s)

#print(diverse)

    