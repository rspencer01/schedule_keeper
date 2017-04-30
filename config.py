##
# @namespace config
#
# System used for loading configurations from files.

import copy

## Obtains some stock standard global variables for the
# configuration file to assume are present.
#
# The available variables are
#
# * `git_branch` : The name of the current branch
# * `git_hash`   : The SHA hash of the current commit
def getGlobals():
  branch = None
  commit = None
  ans = {}
  try:
    import subprocess
    import os
    workingDir = os.path.dirname(__file__) or '.'
    branch = subprocess.check_output("git rev-parse --abbrev-ref HEAD".split(), cwd=workingDir).strip()
    commit = subprocess.check_output("git rev-parse HEAD".split(), cwd=workingDir).strip()
  except Exception as e:
    pass
  finally:
    ans['git_branch'] = branch
    ans['git_hash'] = commit
  return ans

## Creates a dictionary object out of a configuration file
#
# Creates a dictionary out of configuration files.  Config
# files should have extension `.cfg` and format
#
#     name   : "someString"
#     age    : someLiteral
#     list   : ['A','list','of','items']
#     global : some_variable
#     # A commented line.
#
# The global variables are passed as an argument to the
# function, and should be a dict-like object.
#
# If the name of the configuration file is not specified,
# the default is `options.cfg`.
def getConfiguration(configFile="options.cfg", _globals={}):
  import datetime
  evalGlobals = {'datetime': datetime}
  ans = getGlobals()
  lns = open(configFile, "r").readlines()
  for j in range(len(lns)):
    lns[j] = lns[j].strip()
    if lns[j] == '':
      continue
    if lns[j][0] == '#':
      continue
    lns[j] = lns[j].split(':')
    ans[lns[j][0].strip()] = eval(':'.join(lns[j][1:]), evalGlobals, ans)
  return ans

# Execute a module test
if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1:
    print getConfiguration(sys.argv[1])
  else:
    print getConfiguration()
