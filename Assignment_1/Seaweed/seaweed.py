n, k = map(int, input().split())
def taobien(n, k):
    n0, n1 = n,2*n
    if k == 1:
        return n1
    for i in range(k-1):
        n2 = 3*n1 - n0
        n0 = n1
        n1 = n2
    return n2%1000000007
print(taobien(n,k))