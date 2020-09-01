t = int(input())

for _ in range(t):
    s = int(input())
    tm = 0
    while(s != s % 10):
        tm += (s - s % 10)
        s = (s - s % 10)//10 + s % 10
    tm += s
    print(tm)
