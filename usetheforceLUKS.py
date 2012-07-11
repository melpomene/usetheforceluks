#!/usr/bin/python
import sys
import itertools
import os

f = open('wordlist', 'w')
permlist = open("permutations.txt", 'r')
words = [w.strip() for w in permlist]
for i in range(1, len(words)+1):
    for l in itertools.permutations(words, i):
        s = str( "".join(l) + "\n")
        f.write(s)

print "Password list saved as wordlist."

#device = raw_input("Enter the device that is LUKS encrypted eg :/dev/sda2> ")
#print "Now attempting to Brute Force LUKS password using the following wordlist." , options.wordlist
#os.system('./luks_brute.sh' + " " + options.wordlist + " " + device + " encrypted")

