import csv

path="week2/test1.csv"
# with open(path,"w",encoding='UTF-8',newline="") as file:    #使用r+不会覆盖原本内容，newline=""是为了避免写入空行
#     csv_write=csv.writer(file)
#     csv_write.writerow(["Column1", "Column2", "Column3"])

with open(path,"r",encoding='UTF-8',newline="") as file:
    csv_read=csv.reader(file)
    for line in csv_read:
        print(line)

#将csv文件的读写分开进行