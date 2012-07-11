#!/usr/bin/python
import itertools
import os

"""
	This file generates a list of passwords based on permutations of words found the 
	file permutations.txt. 
	Then it runs the shell script luksbrute.sh which loops through all the passwords 
	and tries to mount the drive. If it is found the password is echoed to the screen. 

	Thanks to dangertux for inspiration and shell script. http://www.whenisfive.com/2012/02/04/brute-forcing-luks/
"""

drive = '/dev/path/to/drive' #i.e /dev/sda1

f = open('wordlist', 'w')
permlist = open("permutations.txt", 'r')
words = [w.strip() for w in permlist]
for i in range(1, len(words)+1):
    for l in itertools.permutations(words, i):
        s = str( "".join(l) + "\n")
        f.write(s)

print "Password list saved as wordlist."

print "Use the force LUKS!"
os.system('./luksbrute.sh  wordlist '+ drive)

