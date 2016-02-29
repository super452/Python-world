def bubble(L):
    listLength = len(L)
    while listLength > 0:
        for i in range(listLength - 1):
            if L[i] > L[i+1]:
                L[i] = L[i] + L[i+1]
                L[i+1] = L[i] - L[i+1]
                L[i] = L[i] - L[i+1]
        listLength -= 1
    print (L)
 
if __name__ == '__main__':
    L = [3, 4, 1, 2, 5, 8, 0]
    bubble(L)
