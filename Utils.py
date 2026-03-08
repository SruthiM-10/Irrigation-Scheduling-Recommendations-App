import joblib
import streamlit as st
import pandas as pd

def load_model(model_type: str):
  model_path = f"Models/{model_type}.pkl"
  model = joblib.load(model_path)
  return model

def load_related_data(user_data, method):
  dataset = pd.read_csv("final_dataset_updated_doi.csv").drop("Unnamed: 0", axis=1)
  dataset = dataset[dataset['irrigation_scheduling_method_standardized'] == method]

  dataset['distance'] = (dataset['latitude_decimal_degrees'] - user_data.loc[0, 'latitude_decimal_degrees'])**2 + \
                        (dataset['longitude_decimal_degrees'] - user_data.loc[0, 'longitude_decimal_degrees'])**2
  min_distance = dataset['distance'].min()
  closest_rows = dataset[dataset['distance'] == min_distance]

  if len(closest_rows) > 1:
    closest_rows = closest_rows[closest_rows['plant_type_standardized_to_10'] == user_data.loc[0, 'plant_type_standardized_to_10']]

  if len(closest_rows) == 0:
    return -1, -1, -1, -1, -1

  closest_row = closest_rows.iloc[0]
  link = closest_row["doi_url"]
  summary, setup_params, method_params = get_conditions(closest_row.index)  
  return closest_row, link, summary, setup_params, method_params

def get_conditions(index):
  dataset = pd.read_csv("experimental_conditions.csv")
  return dataset.loc[index, "summary"], dataset.loc[index, "experimental_setup_params"], dataset.loc[index, "irrigation_method_params"]
  
