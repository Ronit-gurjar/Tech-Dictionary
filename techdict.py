import csv 

"""functions"""

#for list to dictionary
def convert(a):
    it = iter(a)
    res_dct = dict(zip(it,it))
    return res_dct

"""main!!!!!!!"""
with open('word_dict.csv','r',encoding="utf-8")  as dict_file:
    dict_read = csv.reader(dict_file)
    next(dict_read)
    for line in dict_read:
        print(convert(line))
        
