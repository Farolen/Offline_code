
# def reverse(x):
#     str_x = str(x)
#     str_y = ""
#     for i in range(len(str_x)-1,-1,-1):
#         str_y += str_x[i]
#     return int(str_y)

# def check_palin(x):
#     str_x = str(x)
#     str_y = ""
#     for i in range(len(str_x)-1,-1,-1):
#         str_y += str_x[i]
#     return str_x == str_y

# slicing : [start:stop:step]
# given a list a = [0,1,2,3,4,5]
# a[1:4] = [1,2,3]
# a[:3] = [0,1,2]
# a[3:] = [3,4,5]
# a[-3:] = 3 last value = [3,4,5] = a[3:]
# a[:-2] = everything except the last 2 value = [0,1,2,3] = a[:5]
# a[::-1] = reverse(a)
# a[4:1:-1] = for(4->2) = [4,3,2]

def reverse(x):
    return int(str(x)[::-1])

def check_palin(x):
    return str(x) == str(x) [::-1]

n = int(input())

ok = check_palin(n)
count = 0

while(ok != True):
    n = n + reverse(n)
    ok = check_palin(n)
    count += 1

print(n,end=" ")
print(count)
