Use the force, LUKS! 
====================
A LUKS brute force script. 
--------------------------


Once every year the power goes out and my home server is forcefully rebooted. 
It is running Ubuntu with the full disc encryption (LUKS). Since it is so seldom my machine is rebooted I tend to forget the disc encryption password. 

Most often I remember it vaugly as a permutation of words and symbols, so to break my own password I have been forced to use a script (and since this is the second time this happens I thought I'll just put it on github so I do not have to reinvent the wheel every time). 

The script contains a python script to generete the passwordfile from permutation of words/symbols in a file called permutations.txt. 

The bash script (thanks dangertux http://www.whenisfive.com/2012/02/04/brute-forcing-luks/) then loops the password list and tries to mount the drive. 
When it is successfull it echos the password to the terminal and exits. 
