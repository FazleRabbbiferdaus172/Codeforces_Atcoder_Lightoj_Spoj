s = input()
ss = s.lower()
sc = s.upper()
a = sum([ord(c) for c in ss])-sum([ord(c) for c in s])
b = sum([ord(c) for c in s])-sum([ord(c) for c in sc])
if a > b:
    print(sc)
else:
    print(ss)
