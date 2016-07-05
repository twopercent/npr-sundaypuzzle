#!/bin/env python3

'''
http://www.npr.org/2016/07/03/484502061/just-in-time-for-the-4th-heres-a-puzzle-tailor-made-for-the-patio

Take the word FALSE. Divide it between the L and the S. The start of the word is the start of FALL, and the end of the word is the end of RISE. And, of course, "fall" and "rise" are opposites. Do the same thing for the word SHALL. Divide it into two parts, so that the start of it starts one word and the end of it ends another word — and those two words are opposites. The dividing point is for you to discover. There are three different solutions. I want you to find all three.

words is a standard file on all Unix and Unix-like operating systems, and is simply a newline-delimited list of dictionary words. It is used, for instance, by spell-checking programs.[1]
The words file is usually stored in /usr/share/dict/words or /usr/dict/words.
On Debian and Ubuntu, the words file is provided by the wordlist package, or its provider packages wbritish, wamerican, etc. On Fedora and Arch, the words file is provided by the words package.
'''

import requests
import os

WORD = 'shall'
WORDS_DICT = '/usr/share/dict/linux.words'


f = open(WORDS_DICT, 'r')


for divide in range(1,len(WORD)):
    f.seek(0)
    lcount = 0
    rcount = 0
    for dict_word in f.readlines():
        if dict_word[:divide] == WORD[:divide]:
            lcount += 1
        if dict_word[:len(WORD)-divide] == WORD[divide:]:
            rcount += 1
    print(WORD[:divide] + ' <-> ' + WORD[divide:])
    print(str(lcount) + ' ' + str(rcount))


f.close()


#r = requests.get('http://words.bighugelabs.com/api/2/' + API_KEY + '/' + WORD + '/json')

#print(r.status_code)
#print(r.text)
