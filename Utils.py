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
  
  closest_rows = dataset[dataset['plant_type_standardized_to_10'] == user_data.loc[0, 'plant_type_standardized_to_10']]

  if len(closest_rows) > 1:
      closest_rows['distance'] = (closest_rows['latitude_decimal_degrees'] - user_data.loc[0, 'latitude_decimal_degrees'])**2 + \
                                (closest_rows['longitude_decimal_degrees'] - user_data.loc[0, 'longitude_decimal_degrees'])**2
      min_distance = closest_rows['distance'].min()
      closest_rows = closest_rows[closest_rows['distance'] == min_distance]

  if len(closest_rows) == 0:
    return -1, -1, -1, -1, -1

  closest_row = closest_rows.iloc[0]
  link = closest_row["doi_url"]
  summary, setup_params, method_params = get_conditions(closest_row.name)  
  return closest_row, link, summary, setup_params, method_params

def get_conditions(index):
  dataset = pd.read_csv("experimental_conditions.csv")
  return dataset.loc[index, "summary"], dataset.loc[index, "experimental_setup_params"], dataset.loc[index, "irrigation_method_params"]

def get_info(method):
  summary = ""
  resources = ""
  if method == "Soil Moisture-Based":
    summary = """
**Overview:** Soil moisture-based scheduling is a "demand-side" approach. Instead of guessing based on weather forecasts, you use sensors to measure the actual water content within the plant’s root zone. It’s like checking your car's fuel gauge rather than assuming you need gas every 300 miles.

**How it Works:**
* **Measurement:** Sensors (Tensiometers or Capacitance probes) are placed at multiple depths to monitor the active root zone.
* **Thresholds:** You define **Field Capacity** (full) and **Management Allowable Depletion** (the trigger point for watering).
* **Action:** Irrigation is only applied when soil moisture hits the trigger point, ensuring the plant never reaches the wilting point while preventing over-saturation.

**Core Benefits:**
* **Water Efficiency:** Often reduces water consumption by **20–50%**.
* **Disease Prevention:** Reduces root rot and fungal issues caused by over-watering.
* **Nutrient Retention:** Prevents "leaching," where excess water washes expensive fertilizers away from the roots."""

  resources = """
  #### **Technical Manuals**
* [USDA NRCS: Irrigation Water Management](https://www.nrcs.usda.gov/resources/guides-and-instructions/irrigation-water-management-plan) - National standards for moisture-monitoring plans.
* [UCANR: Soil Moisture Monitoring Guide](https://ucanr.edu/sites/irrigation/Irrigation_Scheduling/Soil_Moisture_Monitoring/) - A deep dive into sensor types and data interpretation.

#### **Practical Tools**
* [USDA Soil Texture Triangle](https://www.nrcs.usda.gov/sites/default/files/2022-09/The-Soil-Texture-Triangle.pdf) - Essential for understanding your soil's water-holding capacity.
* [MSU Extension: Sensor Setup Guide](https://www.canr.msu.edu/news/using-soil-moisture-sensors-for-irrigation-scheduling) - A beginner-friendly guide to installing your first sensor array.

#### **Scientific Standards**
* [FAO Crop Evapotranspiration (Paper 56)](https://www.fao.org/3/x0490e/x0490e00.htm) - The global gold standard for soil-water-crop relationships.
  """

  return summary, resources
  
