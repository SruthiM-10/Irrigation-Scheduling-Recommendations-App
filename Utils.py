import pickle
import streamlit as st

def load_pickle_files(model_path: str) --> object:
  with open(model_path, "rb") as f:
    model = pickle.load(f)
  return model
