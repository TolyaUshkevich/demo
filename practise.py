def find_annagrams(first, second):
    first = set(first)
    second = set(second)
    if ' ' in first:
        first.remove(' ')
    if ' ' in second:
        second.remove(' ')
    count = 0
    for i in first:
        if i in second:
            count += 1
    if count == len(first) and count == len(second):
        return 'ok'
    else:
        return 'non'
print(find_annagrams(input(), input()))