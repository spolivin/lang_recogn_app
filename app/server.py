from typing import Any

import numpy as np
from fastapi import FastAPI
from io_dataclasses import PredictionOutput, SentenceInput
from transformers import pipeline
from uvicorn import Config, Server

# Instantiating a FastAPI application
app = FastAPI()

# Downloading the model from HuggingFace
bert_pipeline = pipeline(model="spolivin/lang-recogn-model")


@app.get("/")
def home() -> dict[str, str]:
    """Displays a message when sending a GET request."""
    return {
        "status": "OK",
        "task": "language-recognition",
        "model_version": "0.0.1",
    }


@app.post("/predict", response_model=PredictionOutput)
def predict(sentence: SentenceInput) -> dict[str, Any]:
    """Displays the prediction result when sending a POST request."""
    # Applying the pipeline on some text
    prediction_results = bert_pipeline(sentence.text)[0]
    # Retrieving predicted language and probability
    language = prediction_results["label"]
    probability = np.round(prediction_results["score"], 3)

    return {"language": language, "probability": probability}


if __name__ == "__main__":
    config = Config(app=app, port=80)
    server = Server(config=config)
    server.run()
