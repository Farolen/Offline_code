
def reverse(x):
    str_x = str(x)
    str_y = ""

    for i in range(len(str_x)-1,-1,-1):
        str_y += str_x[i]
    return int(str_y)

def check_palin(x):
    str_x = str(x)
    str_y = ""
    for i in range(len(str_x)-1,-1,-1):
        str_y += str_x[i]
    return str_x == str_y


n = int(input())

ok = check_palin(n)
count = 0

while(ok != True):
    n = n + reverse(n)
    ok = check_palin(n)
    count += 1

print(n,end=" ")
print(count)
