def search(data, left, right, key):
    mid = (left + right)//2
    if data[mid] == key:
        return mid
    if left == right:
        return -1
    if data[mid] > key:
        return search(data, left, mid-1, key)
    else:
        return search(data, mid+1, right, key)
def f(x):
    print(search([1,5,9,14,23,26],0,5,x))

f(5)
#f(26)