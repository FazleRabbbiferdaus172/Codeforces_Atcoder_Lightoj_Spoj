"""
ID: fazle.f1
LANG: PYTHON3
PROG: ride
"""
fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
#fin = open('test.txt', 'r')
#fout = open('testout.txt', 'w')
s1 = fin.readline()
s2 = fin.readline()
s1_sum, s2_sum = 1, 1

for i in s1:
    # print(ord("A"))
    s1_sum *= ord(i) - 64
    s1_sum %= 47

for i in s2:
    s2_sum *= ord(i) - 64
    s2_sum %= 47
#print(s1_sum, s2_sum)
if s1_sum % 47 == s2_sum % 47:
    fout.write("GO\n")
else:
    fout.write("STAY\n")
