#encoding: utf-8
#给定一个函数f（x，list），x代表金钱数，list代表商品的各个价格，比如[1,3,4],代表有三件商品，价格分别为...
#当输入一个x时，函数返回能够购买list中的商品数量

def func(x, alist):
    if x < 0 or alist == [] or alist is None:
        print(" 错误 ")
    else:
        alist.sort()
        t_sum = 0
        num = 0
        for i in alist:
            t_sum += i
            if x >= t_sum:
                num += 1
            else:
                print(num)
                break

