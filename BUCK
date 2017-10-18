from os import path
from hashlib import sha256

def add_include_guard(x):
  name = sha256(x).hexdigest()[0:16]
  genrule(
    name = name,
    out = path.basename(x),
    srcs = [
      'scripts/add-include-guard.py', # Order is important here
      x,
    ],
    cmd = 'python $SRCS > $OUT',
  )
  return ':' + name

mathutils_headers = subdir_glob([
  ('mathutils/include', '**/*.hpp'),
])

cxx_library(
  name = 'mathutils',
  header_namespace = 'mathutils',
  exported_headers = dict([
    (x, add_include_guard(y)) for (x, y) in mathutils_headers.items()
  ]),
  srcs = glob([
    'mathutils/src/**/*.cpp',
  ]),
  licenses = [
    'LICENSE',
  ],
  visibility = [
    'PUBLIC',
  ],
)

cxx_binary(
  name = 'demo',
  srcs = [
    'demo.cpp',
  ],
  deps = [
    ':mathutils',
  ],
)
