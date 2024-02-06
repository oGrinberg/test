"""
Python 3.5 and later
"""


import subprocess

def run_scripts(commandstring):
    result = subprocess.run(commandstring.split(), capture_output=True, text=True, check=False)
    print(result.stdout)
    print(result.stderr)


run_scripts('k3d cluster create local-k8s  --api-port 6550  -p 80:80@loadbalancer --agents 2')