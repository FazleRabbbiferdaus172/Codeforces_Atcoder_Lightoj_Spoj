def print_formatted(number):
    # your code goes here
    diff = len(str(bin(number))[2:])
    # print(diff)
    for i in range(1, number+1):
        print(str(i).rjust(diff), str(oct(i))[2:].rjust(diff), str(
            hex(i))[2:].upper().rjust(diff), str(bin(i))[2:].rjust(diff))
        # print(str(hex(i))[2:].upper())


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
