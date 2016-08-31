#!/usr/bin/python2
# coding: utf-8
import nltk
from nltk import tokenize
from nltk import tag
from nltk import chunk
import codecs
import re
from generatedict import dictt

grammar = r"""
  NP:
    {<.*>+}          # Chunk everything
    }<VBD|IN>+{      # Chink sequences of VBD and IN
  P: {<IN>}           # Preposition
  V: {<V.*>}          # Verb
  PP: {<P> <NP>}      # PP -> P NP

  """

list_h = []
list_h1 = []
list_h2 = []
directory2 = "test.hi.txt"
directory1 = "world_align_final.txt"
cp = nltk.RegexpParser(grammar)
with codecs.open(directory2, encoding='utf-8', mode='r')as f3:
    hline = f3.readlines()
for line in hline:
    spl_str_h1 = re.split(r' ', line)
    data8 = [i.replace('\n', '') for i in spl_str_h1]
    list_h.append(data8)
print list_h

with codecs.open(directory1, encoding='utf-8', mode='r')as f4:
    w_line = f4.readlines()
for line in w_line:
    spl_str_h = re.split(r'\t', line)
    data6 = [i.replace('\n', '') for i in spl_str_h]
    data7 = filter(None, data6)
    list_h1.append(data7)

# print list_h1[112734]
a = 0
i = 0
q = 0
f1 = open("eng.txt", 'r')
f2 = open("2123234.txt", 'w')
for line in f1.readlines():
    try:
        print line
        i += 1
        print i

        sent = tokenize.sent_tokenize(line)
        # print sent
        sentn = tokenize.word_tokenize(line)
        # print sentn
        tagged_s = tag.pos_tag(sentn)
        # print tagged_s
        tree = chunk.ne_chunk(tagged_s)
        # print tree
        # tree.draw()
        result = cp.parse(tagged_s)
        # print result
        #
        # result.draw()

        for subtree in result.subtrees():
            if subtree.label() == 'PP':
                # print subtree.leaves()
                t = subtree.leaves()
                # print t
                y = len(t)
                # print y
                # contain prepositon
                print t[0][0]
                # contain noun phrase last word
                print t[y-1][0]
                z = t[0][0]
                print dictt[z]
                # hindi meaning of ppreposition
                hin_word_p = dictt[z]
                noun_p = t[y-1][0]
                # get hindi word of noun
                for g in xrange(len(list_h1)):
                    # word aligner get hindi word
                    if noun_p == list_h1[g][0]:
                        print g
                        for n in xrange(len(list_h1[g])):
                            for k in xrange(len(list_h[q])):
                                 # matched with output file
                                    if list_h1[g][n] == list_h[q][k]:
                                        # print list_h[0][k]
                                        p1 = list_h[q][k]
                                        a = 1
                                        break
                                    else:
                                        a = 0
                    if a:
                        break
                    else:
                        continue

                for k in xrange(len(list_h[q])):
                     # matche hindi word if preposition found append nest word
                    if hin_word_p == list_h[q][k]:
                        k += 1
                        list_h2.append(list_h[q][k])
                    elif p1 == list_h[q][k]:
                        # append noun phrase after preposition appen
                        list_h2.append(list_h[q][k])
                        list_h2.append(hin_word_p)
                    else:
                        list_h2.append(list_h[q][k])




        # for b in list_h2:
        #     print b
        #     f2.write(b.encode('utf-8'))
        #     f2.write(" ")
        # f2.write("\n")
         # print in file after change
        if len(list_h2) == 0:
            for d in list_h[q]:
                f2.write(d.encode('utf-8'))
                f2.write(" ")
            f2.write("\n")
        else:
             # pritnin file after no change
            for b in list_h2:
                print b
                f2.write(b.encode('utf-8'))
                f2.write(" ")
            f2.write("\n")
    except:
        for b in list_h2:
            print b
            f2.write(b.encode('utf-8'))
            f2.write(" ")

        f2.write("\n")
        list_h2 = []
        continue



        # f2.write(str(dictt[z]))
        # f2.write("\n")
        # f2.write(str(t[y-1][0]))
        # f2.write("\n")
    list_h2 = []
    q += 1


f2.close()
f1.close()
f3.close()
f4.close()
