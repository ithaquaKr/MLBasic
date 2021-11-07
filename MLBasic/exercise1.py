def evenDigitsNumber(arr):
    result = 0
    for a in arr:
        count = 0
        mark = a
        while mark > 0:
            mark /= 10
            count += 1
        if count % 2 == 0:
            result += 1
    return result

arr = [12,345,2,6,7869]
print(evenDigitsNumber(arr))

