def modify_list(l1):
    l2 = []
    for i in l1:
        if i % 2 == 0:
            l2.append(int(i//2))
    l1.clear()
    for i in l2:
        l1.append(i)