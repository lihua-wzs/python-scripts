name=input("姓名：")
age=int(input("年龄："))
sex=input("性别：")
#加入检测
if age>120 or age<0:
    print("输入的年龄不符合常理，请重新输入！")
elif sex !="男"  and sex !="女":
    print("输入的性别不符合常理，请重新输入！")
    
else:
    print("姓名:{},年龄：{},性别：{}".format(name,age,sex))

