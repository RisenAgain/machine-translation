#!/usr/bin/python2
# coding: utf-8
import nltk
from nltk import tokenize
from nltk import tag
from nltk import chunk
import codecs
import re
from generatedict import dictt


# for getting noun phrase and preposition

grammar = r"""
  NP:
    {<.*>+}          # Chunk everything
    }<VBD|IN>+{      # Chink sequences of VBD and IN
  P: {<IN>}           # Preposition
  V: {<V.*>}          # Verb
  PP: {<P> <NP>}      # PP -> P NP

  """


cp = nltk.RegexpParser(grammar)

i = 0
f1 = open("test.en.text", 'r')
for line in f1.readlines():
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
        print tree
        #tree.draw()
        result = cp.parse(tagged_s)
        #result.draw()

        for subtree in result.subtrees():
                if subtree.label() == 'PP':
                         print subtree.leaves()
                         t = subtree.leaves()
                         print t
        break
f1.close()

