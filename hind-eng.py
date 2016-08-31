#!/usr/bin/python2
# coding: utf-8
import codecs
import re

# file where english sentences are present with alignment score
directory1 = "eng_align.txt"

#file where hindi sentences are present
directory2 = "hindisent.txt"

#list for containing english word
list_1 = []

#list for containing hindi word 
list_2 = []

#list for containing all hindi sentences
list_hin = []

#list for containing english and corresponding hindi word.
list_final = []

#read all hindi sentences and put it into list_hin list
with codecs.open(directory2, encoding='utf-8', mode='r')as f_two:
    hi_line = f_two.readlines()
for line in hi_line:
    spl_str_hi = re.split(r' ', line)
    list_hin.append(spl_str_hi)

# for iterating hindi sentences from list
j = 0

#get english word with alignment score

with open(directory1, 'r') as f_one:
    data = f_one.readlines()
for line_one in data:
    print line_one
    spl_str = re.split(r' ', line_one)
    # print spl_str

# preprocess the sentences
    data1 = [i.replace('{', '') for i in spl_str]
    data2 = [i.replace('}', '') for i in data1]
    data3 = [i.replace('(', '') for i in data2]
    data4 = [i.replace(')', '') for i in data3]
    data5 = filter(None, data4)
    print data5
    x = (len(data5))
    i = 0
    while i < x-1:
# get english word
        list_1.append(data5[i])

        i += 1

# get corresponding hindi word
        while data5[i].isdigit():
            p = int(data5[i])
            t = p-1
            print t
            print j
            try:
                list_2.append(list_hin[j][t])
            except:
                i += 1
                continue
            i += 1
        for l in list_1:
            list_final.append(l)
        print list_1
        for k in list_2:
            list_final.append(k)
        print list_2
        print list_final
        f1 = open("word1234.txt", 'a')
        for wd in list_final:
            try:
                f1.write(wd.encode('utf-8'))
                f1.write("\t")
            except:
                continue
        f1.write("\n")

# empty the list

        list_2 = []
        list_1 = []
        list_final = []
    j += 1

f_one.close()
f_two.close()
f1.close()
