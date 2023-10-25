# OpenVINO Model Server Demo

Source - [https://blog.openvino.ai/blog-posts/deploy-ai-inference-with-openvino-tm-and-kubernetes](https://blog.openvino.ai/blog-posts/deploy-ai-inference-with-openvino-tm-and-kubernetes)

## Create KinD cluster
```bash
kind create cluster --config kind/kind-config.yaml
```

## Install Operator Lifecycle Manager
```bash
curl -sL https://github.com/operator-framework/operator-lifecycle-manager/releases/download/v0.25.0/install.sh | bash -s v0.25.0
```

## Install OpenVINO operator
```bash
kubectl create -f https://operatorhub.io/install/ovms-operator.yaml
```

```bash
kubectl get csv -n operators 
NAME                       DISPLAY                     VERSION   REPLACES                   PHASE 

openvino-operator.v1.1.0   OpenVINO Toolkit Operator   1.1.0     openvino-operator.v1.0.0   Succeeded 
```

## Deploy sample OpenVINO model server
The OpenVINO model server serves a ResNet-50 image classification model from the locally mounted file system.

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

## Build and run inference app

Build app docker image 
```bash
docker build -t my-python-app:0.1.0 ./python-app/
```

Load image
```bash
kind load docker-image my-python-app:0.1.0
```

Deploy app
```bash
kubectl apply -f python-app/python-deployment.yaml
```

Check app logs
```bash
POD_NAME=$(kubectl get pods -l app=python-app -o jsonpath="{.items[0].metadata.name}")
kubectl logs $POD_NAME
Test app
Detected class: 340
```
