import joblib
import streamlit as st

def load_model(model_type: str):
  model_path = f"Models/{model_type}.pkl"
  model = joblib.load(model_path)
  return model
