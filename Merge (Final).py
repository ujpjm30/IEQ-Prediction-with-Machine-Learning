#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
sensor_csv = os.path.join(desktop, "combined_sensor_data_all_columns.csv")
survey_csv = os.path.join(desktop, "Kendeda_CBE_Survey_February_10_2025 2.csv")

def find_datetime_col(df, thresh=0.5):
    for c in df.columns:
        if pd.to_datetime(df[c], errors="coerce").notna().mean() >= thresh:
            return c
    raise ValueError("None.")


sensor_sample = pd.read_csv(sensor_csv, nrows=100)
sensor_time_col = find_datetime_col(sensor_sample)

df_sensor = pd.read_csv(sensor_csv, parse_dates=[sensor_time_col], encoding="utf-8")
df_sensor.rename(columns={sensor_time_col: "timestamp"}, inplace=True)

if pd.api.types.is_datetime64tz_dtype(df_sensor["timestamp"]):
    df_sensor["timestamp"] = df_sensor["timestamp"].dt.tz_convert(None)

start_ts = pd.to_datetime("2024-09-06")
end_ts   = pd.to_datetime("2024-11-14 23:59:59")
df_sensor = df_sensor[(df_sensor["timestamp"] >= start_ts) &
                      (df_sensor["timestamp"] <= end_ts)]

df_sensor = df_sensor.set_index("timestamp")\
                     .loc[~df_sensor.index.duplicated(keep="first")]\
                     .sort_index()\
                     .reset_index()

df_survey_raw = pd.read_csv(survey_csv, encoding="utf-8")
preferred_cols = ["Start Data", "Start Date", "StartDate"]
survey_time_col = next((c for c in preferred_cols if c in df_survey_raw.columns),
                       find_datetime_col(df_survey_raw))

df_survey = df_survey_raw.copy()
df_survey[survey_time_col] = (
    pd.to_datetime(df_survey[survey_time_col], errors="coerce", utc=True)
      .dt.tz_convert(None)
)
df_survey = df_survey.dropna(subset=[survey_time_col])


df_survey["sensor_time"] = df_survey[survey_time_col] - pd.Timedelta(minutes=15)


df_sensor_sorted = df_sensor.sort_values("timestamp")
df_survey_sorted = df_survey.sort_values("sensor_time")

merged = pd.merge_asof(
    df_survey_sorted,
    df_sensor_sorted,
    left_on="sensor_time",
    right_on="timestamp",
    direction="nearest",
    tolerance=pd.Timedelta(seconds=30) 
)


merged_final = merged.dropna(subset=["timestamp"])

# ──────────────────────────────────────────────────────────────
# 5. 결과 저장
# ──────────────────────────────────────────────────────────────
out_csv = os.path.join(desktop, "merged_20240906-20241114.csv")
merged_final.to_csv(out_csv, index=False, encoding="utf-8")

print(f"✅ Complete → {out_csv}")

