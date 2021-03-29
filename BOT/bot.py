n = int(input())
lst = [int(i) for i in input().split()]
pre_sum = 0
cur_sum = 0
start = 0
_end = 0
for i in range(n):
    cur_sum = cur_sum + lst[i]
    if pre_sum < cur_sum:
        pre_sum = cur_sum
        _end = i
        cur_start = start
    if cur_sum < 0:
        cur_sum = 0
        start = i +1
print(cur_start+1,_end+1,pre_sum)