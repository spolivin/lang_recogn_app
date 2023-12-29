from pydantic import BaseModel


class SentenceInput(BaseModel):
    """Expected input dataclass."""

    text: str


class PredictionOutput(BaseModel):
    """Expected output dataclass."""

    language: str
    probability: float
