Use the force, LUKS! 
====================
A LUKS brute force script. 
--------------------------

The script contains a python script to generate the password file from permutation of words/symbols in a file called permutations.txt. 

The bash script (thanks dangertux http://www.whenisfive.com/2012/02/04/brute-forcing-luks/) then loops the password list and tries to mount the drive. 
When it is successful it echos the password to the terminal and exits. 
