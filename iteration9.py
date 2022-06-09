# 正直角形狀星星
high = 5
n = 1
while n <= high:
    print('*' * n , '\n')
    n += 1
print('--------')

# 倒直角形狀星星
n = high
while n > 0:
    print(' ' * (high - n),'*' * n , '\n')
    n -= 1
print('--------')

# 聖誕樹形狀星星
n = 1
while n <= high:
    s = high - n
    l = n * 2 - 1
    print(' ' * s, '*' * l, '\n')
    n += 1


