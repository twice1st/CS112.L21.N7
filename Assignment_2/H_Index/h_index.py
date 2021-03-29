n = int(input())
x = list(map(int, input().split()))

def H_Index(n, x):
    x.sort(reverse=True)
    h_index = 0
    for i in range(n):
        if x[i] >= i + 1:
            h_index += 1
        else:
            break
    return h_index

print(H_Index(n, x))