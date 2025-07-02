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



## Steps 

I first create the code for querying the model.
The instruction says we need to use the following model:
`https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english`
I start by taking the code snippet from HuggingFace documentation.
Then, I create a test file with three initial unit test.
There are executed with the command:

``` 
poetry run pytest 
```

