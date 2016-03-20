#给定一个n和一个1-100的数组，从数组中任取两个数i、j，使得n=i+j，打印出所有i和j的可能值
def func(n):
    for i in range(1, 101):
        for j in range(1, 101):
            print (i, j)
