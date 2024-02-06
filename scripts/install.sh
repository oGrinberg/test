#!/usr/bin/env sh

sh $(dirname "$0")/build.sh
sleep 5
k3d image import docker.io/test/fastapi:1.0 -c local-k8s
sleep 30
helm upgrade --install fastapi $(dirname "$0")/../helm/fastapi --create-namespace --namespace test
