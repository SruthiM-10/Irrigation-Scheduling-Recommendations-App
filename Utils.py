import joblib
import streamlit as st
import pandas as pd

def load_model(model_type: str):
  model_path = f"Models/{model_type}.pkl"
  model = joblib.load(model_path)
  return model

def load_related_data(user_data):
  dataset = pd.read_csv("final_dataset_updated_doi.csv")
  dataset = dataset[dataset['irrigation_scheduling_method_standardized'] == user_data.loc[0, 'irrigation_scheduling_method_standardized']]

  dataset['distance'] = (dataset['latitude_decimal_degrees'] - user_data.loc[0, 'latitude_decimal_degrees'])**2 + \
                        (dataset['longitude_decimal_degrees'] - user_data.loc[0, 'longitude_decimal_degrees'])**2
  min_distance = dataset['distance'].min()
  closest_rows = dataset[dataset['distance'] == min_distance]

  if len(closest_rows) == 1:
    return closest_rows

  closest_rows = closest_rows[closest_rows['plant_type_standardized_to_10'] == user_data.loc[0, 'plant_type_standardized_to_10']]
  if len(closest_rows) == 1:
    return closest_rows

  if len(closest_rows) == 0:
    return -1
  return closest_rows.iloc[0]
  
