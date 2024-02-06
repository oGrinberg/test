"""
Python 3.5 and later
"""


import subprocess
import os
import signal
import sys
import time

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

def run_scripts(commandstring):
    result = subprocess.run(commandstring.split(), capture_output=True, text=True, check=False)
    print(result.stdout)
    print(result.stderr)

dir_path = os.path.dirname(os.path.realpath(__file__))
app_path = os.path.join(dir_path, 'config', 'servicemonitor.yaml')
print(app_path)

run_scripts("helm repo add prometheus-community https://prometheus-community.github.io/helm-charts")
run_scripts("helm repo update")
run_scripts("helm upgrade --install kube-prometheus-stack prometheus-community/kube-prometheus-stack --version 56.6.0 --create-namespace --namespace monitoring")
print("Please wait for the application to launch, startup time is 2.5 minutes")
time.sleep(150)
run_scripts(f"kubectl apply -f {app_path} -n monitoring")


print("prometheus-operated http://127.0.0.1:9090/ ")
print("prometheus-stack-grafana user:[admin] pass:[prom-operator] http://127.0.0.1:3000/ ") 
print(f"started at {time.strftime('%X')}")
start = time.time()



try:
    signal.signal(signal.SIGINT, signal_handler)
    print('For exit Ctrl+C')
    commands = [
        "kubectl -n monitoring port-forward svc/prometheus-operated 9090:9090", 
        "kubectl -n monitoring port-forward svc/kube-prometheus-stack-grafana 3000:80"
        ]
    procs = [ subprocess.Popen(i, shell=True) for i in commands ]
    for p in procs:
        p.wait()
except:
  print(" ")
finally:
    end = time.time()
    print(f"finished at {time.strftime('%X')}")
    print(f'Time: {end-start:.2f} sec')
    sys.exit(0)
