s = []
validate = ["H", "2B", "3B", "HR"]
for _ in range(4):
    s.append(input())

for i in validate:
    if i not in s:
        print("No")
        break
else:
    print("Yes")
