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
duplicates = 1000
slots = n_lines / duplicates
#f = pd.read_csv("C:\\Users\\Betglad\\Desktop\\adm_hw04\\passwords2.txt", delimiter="\n")

path = 'C:\\Users\\Betglad\\Desktop\\adm_hw04\\passwords2.txt'
with open(path, 'r', encoding='utf-8') as f:
    #head = [next(f) for x in range(50)]
    for s in range(10000):
        lst = []
        asc = toAscii(next(f))
        lst.append(asc)
        # division method
        #lst.append(int(asc % slots))       
        # multiply method
        w = 32                      # machine word size
        A = 0.2345                  # 0 <= A <= 1 (or better A to be <= s (with 0 <= s <= 2^w))
        frac = (asc * A) % 1        # taking fractional part from multiplication
        frac = int(frac * slots)    # taking the floor part from the multiplication
        lst.append(frac)
        diz_ascii[next(f)] = lst
        
diz_slots = {}

for i in range(int(slots)):
    diz_slots[i] = [k.replace('\n', '') for k, v in diz_ascii.items() if v[1] == i]    

for k, v in diz_slots.items():
    print(k, v)


#num_lines = sum(1 for line in open('C:\\Users\\Betglad\\Desktop\\adm_hw04\\passwords2.txt', 'r', encoding='utf-8'))
#[print(l) for l in head]
#print(num_lines)    
#print(len(head))
