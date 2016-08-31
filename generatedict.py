#!/usr/bin/python2
# coding: utf-8

import codecs
from collections import OrderedDict

# filename in which preposition and their meaning is present
directory = "postp.txt"
# create a list for keeping all data
data = []

with codecs.open(directory, encoding='utf-8', mode='r') as flp:
    data1 = flp.readlines()

# print data1

# removing \n from list

data = [j.replace('\n', '') for j in data1]

# print data

# creating a dictionary for preposition and postposition

dictt = OrderedDict()
for i in xrange(len(data)):
    try:
        dictt[data[i]]=data[i+1]
    except:
        continue

# print dictt['above']

flp.close()
