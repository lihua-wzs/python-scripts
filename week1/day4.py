import os
def read_target_line(path,target_line):
    with open(path, "r") as file:
        lines=file.readlines()
        if target_line>1 and target_line<=len(lines):
            print(lines[target_line-1].strip())
        else:
            print("超出范围！")

def create_file(path):
    if os.path.isfile(path):
        print("该文件已存在，请重新输入文件名")
    else:
        with open(path,"w") as file:
            print("文件创建成功!")

path="week1/test.txt"
read_target_line(path,2)
new_path="week1/new_file.txt"
create_file(new_path)
with open(new_path,"w") as file:
    file.write("this is a new file created by python\nIt is intresting!")