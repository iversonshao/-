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
#def f(x):
    #print(search([1,5,9,14,23,26],0,5,x))    

def f():
    data = [1,5,9,14,23,26]
    my_dict={}
    my_dict[9]= search(data, 0, 5, 9)
    my_dict[1]= search(data, 0, 5, 1)
    my_dict[4]= search(data, 0, 5, 14)
    print(my_dict)
    print(data[1:5:2])
#f(5)
#f(26)

f()