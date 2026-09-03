def get_count(s):
    count_dict={}
    for char in s:
        if  char in count_dict:
            count_dict[char]+=1
        else:
            count_dict[char]=1
    print(count_dict)

s="hello world,my name is python"
get_count(s)