# 文件名:    001
# 作者:      1740133524
# 创建时间:      2018/3/9

# 有四个数字：0、1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 请将数目输出来，并这些数打印出来，每个答案请以换行符分隔~~

zongshu = 0

i1 = 1
i2 = 0
i3 = 0
while i1 < 5:
    while i2 < 5:
        if i2 != i1:
            while i3 < 5:
                if i3 != i2 and i3 != i1:
                    print (i1 * 100 + i2 * 10 + i3)
                    zongshu += 1
                    i3 += 1
                else:
                    i3 += 1
            i2 += 1
            i3 = 0
        else:
            i2 += 1
    i1 += 1
    i2 = 0
print ('总数:', zongshu)
