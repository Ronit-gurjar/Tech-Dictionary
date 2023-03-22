import csv 

word_dict = dict()

"""functions"""
#for list to dictionary
def convert(a):
    it = iter(a)
    res_dict = dict(zip(it,it))
    word_dict.update(res_dict)
    return res_dict

"""main!!!!!!!"""
with open('word_dict.csv','r',encoding="utf-8")  as dict_file:
    dict_read = csv.reader(dict_file)
    next(dict_read) #skiping the first line
    for line in dict_read:
        convert(line)

#accessing the dictionary
for a in word_dict:
    print(a,"=",word_dict[a])
