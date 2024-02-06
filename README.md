Readme
=========================

Task
-------

From a provided folder containing text documents, select and process 4 articles of your choice. Your program should identify and return the most common words in these articles. Ensure to specify the chosen articles in your program.

The tools required
-------
* Docker
* Git

Requirement
-------
* free ports 80,9090,3000 on localhost

Run
--------

Steps for run. Run in console:<br>
python:
* python3 start.py
* python3 test.py

bash:
* chmod +x start.sh
* ./start.sh

Monitoring
--------

Monitoring will be available after the script (start.py) is completed.:
* prometheus http://127.0.0.1:9090/
* grafana http://127.0.0.1:3000/  user:[admin] pass:[prom-operator] 

Tested
------
Versions of pre-installed software on which testing was performed
* Tested on mac os.
* Docker desktop Version 4.27.1 
* git version 2.40.1 

Documentation
--------

* https://git-scm.com/
* https://kubernetes.io/
* https://helm.sh/
* https://k3d.io/
* https://fastapi.tiangolo.com/
