
def cheWu():
    # 读取文件内容（车务工单号）
    f = open("E:\\pyfiles\\windseeker\\src\\test_cw\\chewudata\\data.txt", "r")   # 设置文件对象
    data = f.readlines()   # 直接将文件中按行读到list里，效果与方法2一样
    f.close()             # 关闭文件
    return data


if __name__ == "__main__":
    a = cheWu()
    print(a[0])
