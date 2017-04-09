def array_left_rotation(a, n, k):
    size = len(a)
    new_a = []
    for i in range(size):
        index = i + k
        if index > size - 1:
            index -= (size)
        new_a.append(a[index])
    return new_a


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
