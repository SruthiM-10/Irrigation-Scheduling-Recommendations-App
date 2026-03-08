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
* [USDA NRCS: Irrigation Water Management](https://www.nrcs.usda.gov/sites/default/files/2022-09/Irrigation_Water_Management_449_CPS_9_2020.pdf) - National standards for moisture-monitoring plans.
* [UCANR: Soil Moisture Monitoring Guide](https://ucanr.edu/sites/default/files/2010-07/20513.pdf) - A deep dive into sensor types and data interpretation.
* [MSU Extension: Sensor Setup Guide](https://extension.msstate.edu/publications/irrometer-watermark-series-installation-procedures) - A beginner-friendly guide to installing your first sensor array.
  """
elif method == "Evapotranspiration-Based":
  summary = """
**Overview:** Evapotranspiration-based (ET) scheduling is a "supply-side" approach often called the **Checkbook Method**. It calculates how much water is "spent" by the crop and the sun each day and "deposits" that exact amount back into the soil via irrigation.

**How it Works:**
* **The Formula:** It combines **Evaporation** (water lost from soil) and **Transpiration** (water used by the plant).
* **Reference ET ($ET_o$):** Uses weather data (temperature, humidity, wind, solar radiation) from local stations or satellite data.
* **Crop Coefficient ($K_c$):** Multiplies the weather data by a factor specific to your plant (e.g., Maize needs more water during silking than as a seedling).
* **Action:** You maintain a "water balance" sheet. When the cumulative ET loss exceeds a set limit (e.g., 50% depletion), you irrigate.

**Core Benefits:**
* **Automation Ready:** Does not require burying sensors; can be managed entirely via weather station data or apps.
* **Precision:** Highly effective for large-scale operations where soil variability makes sensor placement difficult.
* **Predictive:** Allows you to plan irrigation several days in advance based on weather forecasts."""

        resources = """
#### **Technical Manuals**
* [FAO Irrigation & Drainage Paper 56](https://www.fao.org/4/x0490e/x0490e00.htm) - Guidelines for computing crop water requirements
* [USDA NRCS: ET-Based Scheduling Guide](https://www.nrcs.usda.gov/sites/default/files/2023-06/Montana-Irrigation-Scheduling-Recordbook.pdf) - Official guide on using weather data for water management.

#### **Practical Tools**
* [OpenET Database](https://etdata.org/) - Database of reference evapotranspiration values
* [ASCE Standardized Reference ET Equation](https://ascelibrary.org/doi/book/10.1061/9780784408056) - The standardized mathematical approach used by modern weather stations.
* [UNL Extension: The Checkbook Method](https://extensionpubs.unl.edu/publication/ec709/2009/pdf/view/ec709-2009.pdf) - A practical guide on keeping a water balance sheet.
* [Water Balance Irrigation Scheduling in Florida](https://ufdc.ufl.edu/IR00001504/00001/pdf) - Outlines how crop water requirements are used in this scheduling method
"""

elif method == "Deficit/Partial Irrigation":
  summary = """
**Overview:** Deficit Irrigation (DI) is a sophisticated water-management strategy where the crop is intentionally exposed to a controlled level of water stress. Instead of aiming for maximum water input, you aim for maximum **Water Use Efficiency (WUE)** and crop quality.

**How it Works:**
* **Strategic Timing:** Water is withheld during growth stages that are "drought-tolerant" (like early vegetative growth or late ripening) and provided fully during "critical stages" (like flowering or fruit set).
* **PRD (Partial Rootzone Drying):** A variation where one side of the root system is kept dry while the other is irrigated, tricking the plant into closing its stomata to save water without actually starving it.
* **Monitoring:** Requires careful observation to ensure stress doesn't cross the "permanent wilting point."

**Core Benefits:**
* **Resource Conservation:** Significant water savings (often 15-30%) with minimal impact on final harvest weight.
* **Enhanced Quality:** In many crops (like grapes, tomatoes, and stone fruits), mild stress increases sugar concentration (Brix), antioxidants, and flavor profile.
* **Controlled Growth:** Helps manage excessive leaf growth (canopy), leading to better airflow and less disease pressure."""

        resources = """
#### **Technical Manuals**
* [FAO: Deficit Irrigation Practices](https://openknowledge.fao.org/items/d104647f-54d1-49c1-a7f2-3641323cdc65) - An exhaustive guide on implementing DI across different climate zones.
* [UCANR: Regulated Deficit Irrigation (RDI)](https://ucanr.edu/sites/default/files/2010-07/35511.pdf) - Specific protocols for high-value orchard and vineyard crops.
* [Texas A&M: Irrigation Timing During Drought](https://texaslocalproduce.tamu.edu/files/2023/08/EBN-015.-Irrigation-Timing-During-Drought.-Corn-Cotton-and-Sorghum-Furrow-Systems.pdf) - Practical tables for managing drought stress.
"""

elif method == "Conventional/Fixed Scheduling":
  summary = """
**Overview:** Conventional (or Fixed-Interval) irrigation is the traditional approach where water is applied based on a set schedule—such as every Tuesday and Friday—regardless of daily weather changes or specific plant needs.

**How it Works:**
* **Calendar-Based:** Decisions are made based on historical averages or simple observations (e.g., "The top inch of soil feels dry").
* **Static Application:** The system usually applies the same amount of water (e.g., 1 inch) during every session.
* **Low Tech:** Does not require complex sensors or real-time weather data streams, making it easy to manage for beginners or low-resource farms.

**Core Benefits:**
* **Simplicity:** Extremely easy to manage and requires minimal time for decision-making.
* **Predictability:** Labor and energy costs can be scheduled weeks in advance since you always know when the pumps will be running.
* **Stability:** Provides a "safety net" of moisture, though it often leads to over-watering in humid periods and under-watering during heatwaves."""

        resources = """
* [USDA: Irrigation Guide (Standard Practices)](https://www.nrcs.usda.gov/sites/default/files/2022-10/National_Engineering_Handbook_Part_652_Chapter_9.pdf) - A comprehensive look at traditional water application methods.
"""

  elif method == "Plant/Climate Model-Based":
        summary = """
**Overview:** Plant/Climate Model-Based scheduling uses complex computer algorithms to simulate the entire lifecycle of a plant, predicting its water needs by balancing biological growth models with real-time weather forecasts.

**How it Works:**
* **Growth Modeling:** Uses phenology (the study of plant life cycles) to predict when a plant will hit high-water-use stages like silking or fruiting.
* **Environmental Input:** Integrates data from satellite imagery, local weather stations, and soil maps.
* **Predictive Analysis:** Unlike ET-based (which looks at what happened), models look at **what will happen** over the next 5-7 days to optimize water application before the plant ever feels stress.

**Core Benefits:**
* **Maximized Yield:** Tailors water to the exact biological "hunger" of the plant at every stage of its life.
* **Labor Saving:** Fully digital; requires no field-buried sensors that can be damaged by tractors.
* **Resource Optimization:** Excellent for precision agriculture and variable-rate irrigation (VRI)."""

        resources = """
#### **Technical Manuals**
* [USDA: CropSim and Growth Models](https://www.ars.usda.gov/northeast-area/beltsville-md-barc/beltsville-agricultural-research-center/adaptive-cropping-systems-laboratory/docs/models/what-are-crop-simulation-models/) - Explore the software used to model crop responses.
* [FAO: AquaCrop Training Manual](https://www.fao.org/aquacrop/knowledge-resources/training-materials/en) - The industry standard for modeling crop yield response to water.

#### **Practical Tools**
* [ClearAg: Environmental Modeling](https://www.dtn.com/agriculture/agribusiness/clearag/) - Example of a commercial platform using climate models for farming.
* [UC Davis: CropManage Tool](https://cropmanage.ucanr.edu/) - A free online decision-support tool for model-based scheduling.
"""

    elif method == "Specialized Irrigation Delivery":
        summary = """
**Overview:** This method focuses on **How** the water is delivered, prioritizing high-efficiency systems like **Drip, Sub-surface, or Micro-sprinklers**. It moves away from "flooding" the field and toward "feeding" the plant precisely at the base.

**How it Works:**
* **Targeted Delivery:** Water is delivered directly to the root zone via emitters or porous pipes, bypassing the leaves and open soil where evaporation is highest.
* **Low Pressure:** Operates at much lower pressures than big-gun sprinklers, saving significant energy costs.
* **Sub-surface (SDI):** Pipes are buried 6-18 inches underground, keeping the surface bone-dry to prevent weed growth and evaporation.

**Core Benefits:**
* **Extreme Efficiency:** Can reach **90-95% efficiency**, compared to 60% for traditional flood irrigation.
* **Weed Control:** Since the soil surface stays dry, weed seeds between rows never germinate.
* **Fertigation:** Allows you to mix fertilizer directly into the water (Fertigation), feeding the plant exactly what it needs, when it needs it."""

        resources = """
#### **Technical Manuals**
* [USDA NRCS: Microirrigation Guide](https://www.nrcs.usda.gov/sites/default/files/2022-09/Irrigation_System_Microirrigation_441_NHCP_CPS_2020.pdf) - Detailed engineering for drip and micro-delivery.
* [Netafim: Drip Irrigation 101](https://www.netafim.com/globalassets/local/uae/irrigating-the-future-pdfs/drip-irrigation---understanding-the-basics.pdf) - A practical look at the components needed for specialized delivery.
* [Maintenance of Drip Systems](https://www.netafim.com/globalassets/local/uae/irrigating-the-future-pdfs/complete-drip-maintenance-guide.pdf) - How to prevent clogging in high-efficiency systems.
* [ScienceDirect: Subsurface Drip Irrigation](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/subsurface-drip-irrigation) - Academic overview of the benefits of specialized delivery.
"""
  
  return summary, resources
  
