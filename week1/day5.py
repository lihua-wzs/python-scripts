import os
print(os.listdir(r"D:\python脚本学习"))
lit=os.listdir(r"D:\python脚本学习\week1")
path=os.path.join(r"week1",lit[0])
with open(path,"r",encoding="utf-8") as file: 
    lens=len(file.readlines())
    file.seek(0)      #readlines() 读取完后，文件指针会移动到文件末尾，所以需要使用 seek(0) 将文件指针重新定位到文件开头。   
    print(file.read())
    print("行数:%d",lens)
#**Python 用 GBK 编码读取文件，但文件实际不是 GBK（大概率是 UTF-8），里面有 GBK 无法识别的字节 `0x9a`，解码失败。
# **Windows 系统默认很多文本打开是 GBK；但代码里如果文件本身保存为 UTF-8，强行用 `encoding="gbk"` 打开就会报这个错。
