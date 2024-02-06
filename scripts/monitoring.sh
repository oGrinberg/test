#!/usr/bin/env sh

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm upgrade --install kube-prometheus-stack prometheus-community/kube-prometheus-stack --version 56.6.0 --create-namespace --namespace monitoring

sleep 180
kubectl apply -f $(dirname "$0")/config/servicemonitor.yaml -n monitoring

echo "prometheus-operated http://127.0.0.1:9090/ "
echo "prometheus-stack-grafana user:[admin] pass:[prom-operator] http://127.0.0.1:3000/ "
kubectl -n monitoring port-forward svc/prometheus-operated 9090:9090  &
kubectl -n monitoring port-forward svc/kube-prometheus-stack-grafana 3000:80 &
wait