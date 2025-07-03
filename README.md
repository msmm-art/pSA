# Project pSA (Sentiment Analysis) by Matias Martinez

## Installation

This project requires poetry. If you don't have it installed, please install it with

```commandline
 pip install poetry

````


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

Again, we can invoke the service with the following command, each with a different output:

```bash
curl "http://localhost:8000/sentiment?input=I+like+summer"
curl "http://localhost:8000/sentiment?input=I+hate+summer" 
```

### Build the docker with the CI

We also incorporate new steps in the CI to build the docker image and to run the container.
See the successful job [here](https://github.com/msmm-art/pSA/actions/runs/16031773702/job/45233891720)

