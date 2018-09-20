class SeqList:
    import time
    def A(sqlist):
        x = int(input("输入x： "))
        y = int(input("输入y： "))
        seat = sqlist.index(y)
        sqlist.remove(x)
        sqlist.insert(seat - 1, x)

    def B(sqlist):
        x = int(input("输入x： "))
        y = int(input("输入y： "))
        sqlist.remove(x)
        seat = sqlist.index(y)
        sqlist.insert(seat + 1, x)


    sqlist = []
    max = int(input("输入顺序表长度："))
    comm_count = int(input("输入指令个数： "))
    for i in range(0, max):
        sqlist.append(int(input("输入数据： ")))
    print(sqlist)
    for p in range(0, comm_count):
        Comm = input("输入方法名： ")
        if Comm == "A":
             A(sqlist)
        if Comm == "B":
             B(sqlist)

    print(sqlist)

    time.sleep(10)
