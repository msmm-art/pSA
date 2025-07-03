# Project pSA (Sentiment Analysis) by M.Martinez

## Installation

This project requires poetry. If you don't have it installed, please install it with

```commandline
 pip install poetry

````

First, I create a new project with poetry. I name it `pSA` (short for Project Sentiment Analysis).

```commandline
poetry new pSA
```

Now, let's create the environment (We have not specified the dependencies yet)

```commandline
poetry install
```

After that, I have the environment so I can configure it within my IDE.



## Development Steps 

In this section I describe how I implemented the requiered functionality step by step.

### Sentiment Analyzer core and tests
I first create the code for querying the model.
The instruction says we need to use the following model:
`https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english`
I start by taking the code snippet from HuggingFace documentation.
Then, I create a test file with three initial unit test.
There are executed with the command:

``` 
poetry run pytest 
```

### CI for the backend

I first create an initial workflow for the backend. In addition to build the application, it runs the test cases. 
See results of the first execution [here](https://github.com/msmm-art/pSA/actions/runs/16028622995/job/45223037485).

### Now that we have the logic for the sentiment analyzer, I create the API.

First, I start the server with the FastAPI service
```
poetry run uvicorn psa.Services:app --reload --host 0.0.0.0 --port 8000

```
Then, I do a http invocation to the service
```
 curl "http://localhost:8000/sentiment?input=I+hate+summer"
```

### Incorporating Docker into the project

I create a Dockerfile to containerize the application.
The container is created with the command:

```bash
 docker build -t sentiment-analyzer .  
```
Then, I run the container with the command:

```bash
 docker run -p 8000:80 sentiment-analyzer
```

Again, I can invoke the service with the following command, each with a different output:

```bash
curl "http://localhost:8000/sentiment?input=I+like+summer"
curl "http://localhost:8000/sentiment?input=I+hate+summer" 
```

### Build the docker with the CI

I also incorporate new steps in the CI to build the docker image and to run the container.
See the successful job [here](https://github.com/msmm-art/pSA/actions/runs/16031773702/job/45233891720)

### Kubernetes

I create the Kubernetes' deployment and service manifests.

```
kubectl apply -f k8s/deployment.yaml 
kubectl apply -f k8s/service.yaml   
```

We can observe the status of the deployment (Pods and Services) with commands:

```bash
kubectl get pods
kubectl get service
```

To test locally the service, it is necessary that the service type is set to `NodePort` in the manifest rather than `LoadBalancer`.
Then, I can check the status of the deployment with the command:

``` 
curl "http://localhost:<PORT>/sentiment?input=BAD" 
```

The port <PORT> can be obtained with the command:

```bash
kubectl get svc sentiment-service
```
(Please corroborate that the TYPE is `NodePort` and not LoadBalancer`) 

To deploy it on AWS, then we can keep the TYPE `LoadBalancer`. Importantly, it is required to install the [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.2/deploy/installation/).
Then, the service is accessible via the external IP address  that can be also retrieved with the command `kubectl get svc sentiment-service`.

``` 
curl "http://<External-IP>:<PORT>/sentiment?input=GOOD" 
```
