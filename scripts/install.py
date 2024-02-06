"""
Python 3.5 and later
"""


import subprocess
import os
import time

def run_scripts(commandstring):
    result = subprocess.run(commandstring.split(), capture_output=True, text=True, check=False)
    print(result.stdout)
    print(result.stderr)

dir_path = os.path.dirname(os.path.realpath(__file__))
app_path = os.path.join(dir_path, '..', 'helm', 'fastapi')
print(app_path)
build_path = os.path.join(dir_path, "build.py")

run_scripts(f"python3 {build_path}")
time.sleep(5)
print("k3d image import")
run_scripts("k3d image import docker.io/test/fastapi:1.0 -c local-k8s")
print("Please wait 0.5 minutes")
time.sleep(30)
run_scripts(f"helm upgrade --install fastapi {app_path} --create-namespace --namespace test")

