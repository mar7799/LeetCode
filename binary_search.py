def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while(first <= last):
        midpoint = (first+last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1
    return None

bi = [1,2,3,4,5,6,7,8]

def verfiy(index):
    if index is not None:
        print("Target found at", index)
    else:
        print("Target not found")
result = binary_search(bi,8)
verfiy(result)