#!/usr/bin/env sh

# create cluster
k3d cluster create local-k8s  --api-port 6550  -p "80:80@loadbalancer" --agents 2
