import csv 

"""functions"""

#for list to dictionary
def convert(a):
    it = iter(a)
    res_dct = dict(zip(it,it))
    return res_dct

"""main!!!!!!!"""
with open('t2.csv','r',encoding="utf-8")  as t2_file:
    t2_read = csv.reader(t2_file)
    next(t2_read)
    for line in t2_read:
        print(convert(line))
        
