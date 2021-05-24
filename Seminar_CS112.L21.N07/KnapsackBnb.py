class Item:
    def __init__(self, w, v):
        self.weight = w
        self.value = v

class Node:
    def __init__(self):
        self.level = 0
        self.profit = 0
        self.bound = 0
        self.weight = 0
    def copy(self):
        x = Node()
        x.level = self.level
        x.profit = self.profit
        x.bound = self.bound
        x.weight = self.weight
        return x

def v_div_w(a):
    return a.value/a.weight

def bound(u, n, W, arr):
    if u.weight >= W:
        return 0

    profit_bound = u.profit

    j = u.level + 1
    totweight = u.weight

    while j < n and (totweight + arr[j].weight) <= W:
        totweight += arr[j].weight
        profit_bound += arr[j].value
        j += 1  
    if j < n:
        profit_bound += (W - totweight) * arr[j].value / arr[j].weight 
    return profit_bound

def knapsack(W, arr, n):
    arr.sort(key = v_div_w, reverse=True)
    
    Q = list()
    u = Node()
    v = Node()
    u.level = -1
    u.profit = 0
    u.weight = 0
    Q.append(u)
    maxProfit = 0
    while len(Q) != 0:
        u = Q[0]
        Q.pop(0)
        if u.level == -1:
            v.level = 0     
        if u.level == n-1:
            continue
        v.level = u.level + 1
        v.weight = u.weight + arr[v.level].weight
        v.profit = u.profit + arr[v.level].value
        if v.weight <= W and v.profit > maxProfit:
            maxProfit = v.profit
        v.bound = bound(v, n, W, arr)
        
        t = v.copy()
        if v.bound > maxProfit:
            Q.append(t)
        v.weight = u.weight
        v.profit = u.profit
        v.bound = bound(v, n, W, arr)
        t = v.copy()
        if v.bound > maxProfit:
            Q.append(t)

    return maxProfit




wt = list(map(int, input().split()))
vt = list(map(int, input().split()))
W = int(input())

arr = list()
for x in zip(wt, vt):
    u = Item(x[0], x[1])
    arr.append(u)

n = len(arr)
print(knapsack(W, arr, n))

