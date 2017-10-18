#!/usr/bin/env python
import sys
import shutil
from hashlib import sha256

def hash_file(filename):
  h = sha256()
  with open(filename, 'rb', buffering = 0) as f:
    for b in iter(lambda : f.read(128 * 1024), b''):
      h.update(b)
  return h.hexdigest()

# Get the file path from args
if len(sys.argv) != 2:
  print "Usage: <file_path>"
  sys.exit(1)

file_path = sys.argv[1]

# Hash the file
guard = 'INCLUDED_' + hash_file(file_path)[0:32]

# Output the contents with an include guard to standard out
print '#ifndef ' + guard
print '#define ' + guard + '\n'

with open(file_path, 'r') as f:
  shutil.copyfileobj(f, sys.stdout)

print ''
print '#endif'
