# OpenVINO Model Server Demo


## Create KinD cluster
```bash
kind create cluster --config kind/kind-config.yaml
```

## Install Operator Lifecycle Manager
```bash
curl -sL https://github.com/operator-framework/operator-lifecycle-manager/releases/download/v0.25.0/install.sh | bash -s v0.25.0
```bash

## Install OpenVINO operator
```bash
kubectl create -f https://operatorhub.io/install/ovms-operator.yaml

kubectl get csv -n operators 
NAME                       DISPLAY                     VERSION   REPLACES                   PHASE 

openvino-operator.v1.1.0   OpenVINO Toolkit Operator   1.1.0     openvino-operator.v1.0.0   Succeeded 
```bash

## Deploy sample OpenVINO model server
This deploys an OpenVINO model server with a ResNet-50 image classification model.

```bash
kubectl apply -f deployment/ovms.yaml
```

```bash
kubectl get pods
NAME                           READY   STATUS    RESTARTS   AGE
ovms-sample-7cf68d6b46-rrrw2   1/1     Running   0          16s
```

```bash
kubectl get svc
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
ovms-sample   ClusterIP   10.96.172.239   <none>        8080/TCP,8081/TCP   53s
```
