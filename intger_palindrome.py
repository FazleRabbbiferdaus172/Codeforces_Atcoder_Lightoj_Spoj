n = int(input())
x = n
another = 0

while n:
    t = n % 10
    another = another * 10 + t
    n //= 10
flag = 1
#print("test", another)
while x and another:
    t1, t2 = x % 10, another % 10
    x, another = x // 10, another // 10
    if t1 != t2:
        flag = 0
        break

if flag:
    print("Palindrome")
else:
    print("Not Palindrome")
