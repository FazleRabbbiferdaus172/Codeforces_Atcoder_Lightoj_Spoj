mod = int(1e9) + 7

x, y = map(int, input().split())
n = int(input())
l = [x, y, y-x, -x, -y, x-y]


print(l[(n % 6) - 1] % mod)
