from collections import namedtuple
n = int(input())
fields = input().split()
# print(fields)
fields = ",".join(fields)
marksheet = namedtuple('marksheet', fields)
avg = 0
for i in range(n):
    inp = input().split()
    temp = marksheet(*inp)
    avg += int(temp.MARKS)

print("{:.2f}".format(avg/n))
