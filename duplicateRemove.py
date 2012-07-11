#!/usr/bin/python
import itertools
"""
	Creates permutations of the words in permutations.txt
	This scripts looks in the old wordlist file and doesn't add duplicates of passwords. 
	Thus if you run the script and want to try some new permutations this script is what you use. 
"""

fr = open('wordlist', 'r')
f = open('wordlist', 'w')
permlist = open("permutations.txt", 'r')
words = [w.strip() for w in permlist]
old_words = [w.strip() for w in fr]

for i in range(1, len(words)+1):
    for l in itertools.permutations(words, i):
        s = str( "".join(l) + "\n")
        if s not in old_words:
            f.write(s)
	
