"""
Python 3.5 and later
"""


import subprocess
from sys import platform

def run_scripts(commandstring):
    result = subprocess.run(commandstring.split(), capture_output=True, text=True, check=False)
    print(result.stdout)
    print(result.stderr)



if platform == "linux" or platform == "linux2":
    # linux
    run_scripts("wget -q -O - https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash")
elif platform == "darwin":
    # OS X
    run_scripts("brew install k3d helm kubectl")
elif platform == "win32":
    # Windows...
    run_scripts("choco install k3d -y")
    run_scripts("choco install kubernetes-helm -y")
    run_scripts("choco install kubernetes-cli -y")





