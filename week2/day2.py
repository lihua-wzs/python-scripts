import csv
path_read="week2/score.csv"
great_students=[]    #创建空列表储存成绩合格的学生
#进行筛选成绩合格的学生
with open(path_read,"r",encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    for line in reader:
        if float(line[-1])>=80:
            great_students.append(line)
print(great_students)
#将成绩合格的学生写入新的csv文本
path_write="week2/great_students.csv"
with open(path_write,"w",encoding="utf-8",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(header)
    writer.writerows(great_students)
    print("写入成功！")
#进行验证
with open(path_write,"r",encoding="utf-8") as file:
    reader_lines=csv.reader(file)
    for line in reader_lines:
        print(line)
