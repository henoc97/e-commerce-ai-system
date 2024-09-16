# test_model_training.py
import pytest
from src.model_training import train_model # type: ignore

def test_train_model():
    model = train_model()
    assert model is not None
    assert hasattr(model, 'predict')
