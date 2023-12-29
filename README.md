# Language Recognition Application[FastAPI]

This repository is dedicated to storing the code needed to launch a simple FastAPI application for fast language detection tasks. The core of the application represents the fine-tuned *BERT* model trained and subsequently fine-tuned on large corpuses of multilingual texts.

## Model description

### Base model
The model has been fine-tuned based on `transformers.BertForSequenceClassification` model pretrained on [multilingual texts](https://huggingface.co/bert-base-multilingual-uncased).

The model has been published on *HuggingFace* platform and can be [tested](https://huggingface.co/spolivin/lang-recogn-model) using Pipeline API.

### Dataset

The model has been fine-tuned on [Language Detection](https://www.kaggle.com/datasets/basilb2s/language-detection) dataset taken from *Kaggle*. The dataset includes corpuses of labeled multilingual texts for 17 languages.

### Training procedure

Due to the absence of *GPU* accelerators on the local machine, *Kaggle* platform has been chosen for data analysis and model fine-tuning. The complete description of the analysis conducted can be found in the following [notebook](https://www.kaggle.com/code/sergeypolivin/language-recognition-using-bert).

## Launching the app

### Command line (uvicorn)

In order to be able to launch the application on the local machine, all one can do is firstly install the required dependencies:

```
pip install -r requirements/requirements-server.txt
```

Afterwards, the server can be set up in a pretty straightforward way as follows:

```
python app/server.py
```

This command will start the application on port 80 which can be now seen on `localhost:80`.

### Docker

Running the application via the command line requires having the Python interpreter as well as the dependencies installed. Fortunately, provided that the Docker is already installed and up and running on the local machine, all this can be avoided by making use of Docker images and containers. Having `Dockerfile` in the following repository now enables running the application in the Docker container.

Firstly, we need to build the Docker image via the following command:

```
docker build -t lr_image .
```

As soon as the image has been built, we can now launch the image in an isolated container with the following command:

```
docker run --name lr_container -p 80:80 lr_image
```
> When running the container for the first time, it is recommended not to use `-d` flag, since the model needs to firstly get downloaded from *HuggingFace* to the container so in this case a user will be able to see when the container is ready to be tested.

After that we can immediately test the FastAPI server on port 80.

#### Note

In case of the need to use the container again, it is possible to simply run the following command:

```
docker start lr_container
```

Since the model has already been downloaded into the container, we can immediately test the launched container.

## Application usage

In order to test whether the server has been actually started, we need to go to localhost on any browser which should display the following message on the screen:

```
{"status": "OK", "task": "language-recognition", "model_version": "0.0.1"}
```

Additionally, if we are running the app via the Docker container, it is possible to consult the logs that appeared on the screen or use `docker logs lr_container` (in case of running the existing container) in order to see if everything is running smoothly.

After we have made sure of the server starting, we can use a special feature of FastAPI server and go to `localhost/docs`. Over there, we can now go to `/predict` method and click on "Try it out".

Now, we will see the input window where instead of `string`, we can write for instance the following sentence in Danish language:

```
{
  "text": "Hej Verden!"
}
```

After clicking on "Execute", we will be able see the predicted language as well as the according probability associated with this label:

```
{
  "language": "Danish",
  "probability": 0.94
}
```

## Automatic code style checks

This repository is equipped with an opportunity to check the files before actually registering a commit. For that we need to have two things:

1. **Installed `pre-commit` library and *pre-commit hooks***.

Firstly, we need to install the `pre-commit` library itself which can be downloaded automatically together with all other required dependencies for this repository:

```
pip install -r requirements/requirements.txt
```

After that we need to run the following command to create `hooks` directory in a hidden `.git` folder:

```
pre-commit install
```

2. ***Pre-commit hooks* configuration in `.pre-commit-config.yaml` file**.

Now that we have installed the hooks correctly, we can now create a [configuration file](.pre-commit-config.yaml) for storing different checks that we want to impose on files staged for commit.

In this case, the configuration file includes the following hooks:

| Pre-commit hook | Version | Usage |
| :---------------------- | :---------------------- | :---------------------- |
| *pre-commit-hooks* | 4.3.0 | Trailing whitespaces, end of files, *py*- and *yaml*-files validity, debug statements checks and private key detection |
| *pyupgrade* | 3.10.1 | Code style adjustments in accordance with Python 3.9+ |
| *autoflake* | 2.1.1 | Unused variables and imports removal |
| *isort* | 5.12.0 | Imports sorting and reordering |
| *black* | 23.3.0 | Code formatting |
| *codespell* | 2.2.4 | Word spelling checks |

## References

1. [BERT multilingual base model (uncased)](https://huggingface.co/bert-base-multilingual-uncased)

2. [Language Detection Dataset](https://www.kaggle.com/datasets/basilb2s/language-detection)

[Back to top](#language-recognition-applicationfastapi)
