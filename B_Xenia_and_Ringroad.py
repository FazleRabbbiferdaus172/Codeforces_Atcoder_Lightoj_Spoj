n, m = list(map(int, input().split()))
task = list(map(int, input().split()))

time = 0
here = 1

for i in task:
    if here > i:
        time += n+1 - here
        time += i - 1
    else:
        time += i - here
    here = i
print(time)
