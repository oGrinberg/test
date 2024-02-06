"""
Python 3.5 and later
"""


import subprocess
import os

def run_scripts(commandstring):
    result = subprocess.run(commandstring.split(), capture_output=True, text=True, check=False)
    print(result.stdout)
    print(result.stderr)


dir_path = os.path.dirname(os.path.realpath(__file__))
app_path = os.path.join(dir_path, '..', 'app', 'fastapi')
print(app_path)

run_scripts(f"docker build {app_path} -t test/fastapi:1.0")
