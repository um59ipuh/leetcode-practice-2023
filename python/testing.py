def find_missing_duplicate(arr):
    start_from = 1
    missing = 0
    for n in arr:
        if n != start_from:
            missing = n
            break
        start_from += 1
        
    length = len(arr)
    diff = sum(arr) - (length*(length + 1))//2
    duplicate = missing + diff
    return (missing, duplicate)

print(find_missing_duplicate([1,5,3,4,5,6,7]))