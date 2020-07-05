n = int(input())
s = input()
if s.count('A') == s.count('D'):
    print("Friendship")
elif s.count('A') < s.count('D'):
    print("Danik")
else:
    print("Anton")
