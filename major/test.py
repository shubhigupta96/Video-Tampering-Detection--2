import os
import subprocess
print os.getcwd()
import shutil


print os.path.join(os.path.dirname(os.path.realpath(__file__)),'frames/') 

p = subprocess.Popen(['rm -rf *'], cwd =os.path.join(os.path.dirname(os.path.realpath(__file__)),'frames/'))
p.wait()
# subprocess.check_call(['rm -rf'], cwd =os.path.join(os.path.dirname(os.path.realpath(__file__)),'frames'))
