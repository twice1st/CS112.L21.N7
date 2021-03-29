from collections import Counter
x = input().strip()
count_num = Counter(x)
mod_num = []
mod_num.append([0])
mod_num.append(['1','4','7'])
mod_num.append(['2','5','8'])
mod_num = [[x for x in d if x in count_num] for d in mod_num]
sum_ = sum(int(i)*count_num[i] for i in count_num)
mod_ = sum_%3
if mod_:
    count_digit_same_mode = sum(int(count_num[i]) for i in mod_num[mod_])
    number_del = 1
    if not count_digit_same_mode:
        mod_ = 3 - mod_ 
        number_del= 2
    for i in mod_num[mod_]:
        j = min(number_del, count_num[i])
        number_del-= j
        count_num[i] -= j
for i in sorted(count_num.keys(), reverse=True):
    print(i*count_num[i], end="")