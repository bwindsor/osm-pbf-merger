import sys
import subprocess
import time
import os

def ShowHelp():
    print('')
    print('Usage:')
    print('convert.py INPUT1 [INPUT2 [INPUT3 [ ... ]]] [-o OUTPUT]')
    print('If OUTPUT is not supplied, file out.osm.pbf will be used')
    print('')

    
print(sys.argv)

nargin = len(sys.argv)

if nargin < 3:
    ShowHelp()
    exit(1)

if sys.argv[1]=='--help':
    ShowHelp()
    exit(0)

DATA_DIR = '/data'
    
# Check for output file
num_input_files = nargin - 1
if (sys.argv[nargin-2] == "-o"):
    output_file = sys.argv[nargin]
    num_input_files = num_input_files - 2
else:
    output_file = 'out.osm.pbf'
output_file = os.path.join(DATA_DIR, output_file)
    
if num_input_files < 1:
    ShowHelp()
    exit(1)

# Build command line command
command = ''
command = command + 'osmconvert'

# All files except the final one
for x in range(1, num_input_files):
    file = os.path.join(DATA_DIR, sys.argv[x])
    if not os.path.isfile(file):
        print('File not found: ' + file)
        exit(1)
    command = command + ' <(osmconvert ' + file + ' --out-o5m)'

# Final file
file = os.path.join(DATA_DIR, sys.argv[num_input_files])
if not os.path.isfile(file):
        print('File not found: ' + file)
        exit(1)
command = command + ' ' + file

# Output file
command = command + ' -o=' + output_file

print('Command to run: ' + command)

process = subprocess.Popen(['/bin/bash', '-c', command], stdout=subprocess.PIPE)
for c in iter(lambda: process.stdout.read(1), ''):
    sys.stdout.buffer.write(c)
    sys.stdout.flush()
    if process.poll() is not None:
        exit(process.returncode)