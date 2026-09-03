#提取数组中的偶数
def get_even(num):
    new_num=[]
    for i in num:
        if i%2==0:
            new_num.append(i)
    print(new_num)
#找到数组中的最大值
def get_max(num):
    max=0
    for i in num:
        if i>max:
            max=i
    print(max)

#找到数组的最小值
def get_min(num):
    min=0
    for i in num:
        if i<min:
            min=i
    print(min)
num=[1,2,30,4,5,6,16,31,66,14,0,19,11]

#求取数组的平均值
def get_avg(num):
    sum=0
    for i in num:
        sum+=i
    avg=sum/len(num)
    print(avg)

get_even(num)
get_max(num)
get_min(num)
get_avg(num)