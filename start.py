"""
Python 3.5 and later
"""

import subprocess
import os


scriptslist = [
    "install_tools.py",
    "k3d.py",
    "install.py",
    "monitoring.py",
    ]

def run_scripts(scriptslist):
    for x in scriptslist:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        x_path = os.path.join(dir_path, 'scripts', x)
        print("#####Start#####:" + x_path)
        subprocess.run(["python3", x_path], text=True, check=False)
        print("#####End#####:" + x_path)

try:
    run_scripts(scriptslist)
except:
  print(" ")