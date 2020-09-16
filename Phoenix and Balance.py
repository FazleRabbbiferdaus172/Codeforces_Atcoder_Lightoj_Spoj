for _ in range(int(input())):
    n = int(input())
    hlf = n//2

    one_p = 2**n
    for i in range(1, hlf):
        one_p += 2**i

    two_o = 0

    for i in range(hlf, n):
        two_o += 2**i

    print(abs(one_p-two_o))
