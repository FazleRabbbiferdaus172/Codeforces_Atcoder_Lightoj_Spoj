from ADT.SequenceADT import Sequence
from ADT.utils.listToSequence import listToSequence
from random import randint

def matchNutsAndBolts(ns,bs):
    sortNutsAndBolts(ns,bs,0, ns.size() - 1)

def sortNutsAndBolts(ns,bs, start, end):
    if end<=start:
        return
    pivot = randint(start, end)
    pivot = part(ns,start,end, bs.atRank(pivot).element())
    pivot = part(bs,start,end, ns.atRank(pivot).element())
    sortNutsAndBolts(ns,bs,start,pivot-1)
    sortNutsAndBolts(ns,bs,pivot+1,end)

def part(ns: Sequence, start, end, pvElement):
    p,q = start, end
    current = start
    while current <= q:
        ce = ns.atRank(current).element()
        if ce == pvElement:
            current+=1
        elif ce > pvElement:
            qe = ns.atRank(q).element()
            ns.atRank(current)._element = qe
            ns.atRank(q)._element = ce
            q-=1
        elif ce < pvElement:
            qe = ns.atRank(p).element()
            ns.atRank(current)._element = qe
            ns.atRank(p)._element = ce
            p+=1
            current += 1
    return p
    
ns = listToSequence([4,5,1,7,3,6])
bs = listToSequence([6,4,1,5,7,3])
matchNutsAndBolts(ns,bs)
print(ns)
print(bs)

