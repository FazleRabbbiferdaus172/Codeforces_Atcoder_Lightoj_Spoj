from ADT.SequenceADT import Sequence

def mergeSort(s: Sequence, result) -> Sequence:
    n = s.size()
    if n == 1:
        return s, 0

    mid = n // 2

    s1 = Sequence()
    s2 = Sequence()
    copyTo(s1, s, 0, mid)
    copyTo(s2, s, mid, n)
    s1, i = mergeSort(s1, result)
    s2, j = mergeSort(s2, result)

    x, inv = merge(s1, s2)
    return x, inv + i + j


def copyTo(a: Sequence, b: Sequence, i, j) -> Sequence:
    for i in range(i, j):
        a.insertLast(b.atRank(i))
    return a

def merge(s1: Sequence, s2:Sequence) -> Sequence:
    result = Sequence()
    inv = 0
    while not s1.isEmpty() and not s2.isEmpty():
        if s1.first().element() <= s2.first().element():
            result.insertLast(s1.first().element())
            s1.remove(s1.first())
        else:
            result.insertLast(s2.first().element())
            s2.remove(s2.first())
            inv += 1

    while not s1.isEmpty():
        result.insertLast(s1.first().element())
        s1.remove(s1.first())       
    
    while not s2.isEmpty():
        result.insertLast(s2.first().element())
        s2.remove(s2.first())

    return result, inv

n = Sequence()
for i in [5, 1, 3, 4, 6]:
    n.insertLast(i)

print(mergeSort(n, 0))