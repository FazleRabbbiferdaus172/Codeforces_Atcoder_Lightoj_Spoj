from collections import Counter, defaultdict
T = int(input())
for t in range(T):
    n = int(input())
    dic = Counter(map(int, input().split()))
    ans = defaultdict(int)
    for i in dic:
        for j in dic:
            ans[i + j] += min(dic[i], dic[j])
    print(max(ans.values()) // 2)
