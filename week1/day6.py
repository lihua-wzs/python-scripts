def get_div():
    try:
        num1=float(input("请输入第一个数字："))
        num2=float(input("请输入第二个数字："))
        if num2 == 0:
            print("除数不能为0，请重新输入！")
        else:
            print("%.2f / %.2f = %.3f" %(num1,num2,num1/num2))
    except ValueError:
        print("输入的数字不符合要求，请重新输入！")
#try except 语句用于捕获异常，避免程序因异常而终止运行，如果try中的代码出现异常，则会执行except中的代码，程序不会终止运行。

if __name__ == "__main__":
    get_div()