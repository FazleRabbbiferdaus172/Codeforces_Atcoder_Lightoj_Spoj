def gen_powerset(i, arr=[], result=[]):
    if i <= 0:
        result.append(arr)
        return result
    gen_powerset(i-1, arr, result)
    gen_powerset(i-1, arr + [i], result)
    return result

def get_powerset(x):
    p = gen_powerset(x)
    print(p)

get_powerset(3)