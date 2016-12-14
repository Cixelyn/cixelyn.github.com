from fabric.api import *
from datetime import datetime
from os.path import dirname

def build():
  with lcd(dirname(env.real_fabfile)):
    commit_message = 'Autobuilding on %s' % datetime.now()

    local('rm -rf build')
    local('git clone --depth 1 git@github.com:Cixelyn/cixelyn.github.com.git build')
    local('bundle exec middleman build')

    with lcd('build'):
      local('git add -A')
      local('git commit -m "%s"' % commit_message)
      local('git push')

def clean():
  with lcd(dirname(env.real_fabfile)):
    local('rm -rf build')
 
