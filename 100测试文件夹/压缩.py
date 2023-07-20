def compact(lst):
    return list(filter(bool, lst))


compact([0, 1, False, 2, '', 3, 'a', 's', 34])  # [ 1, 2, 3, 'a', 's', 34 ]

# 代码片段: # https://blog.csdn.net/zhongjunlang/article/details/114318055
