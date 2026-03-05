import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Student Admission Plan.csv", encoding = "utf-8")
print(df.head())


df = df.dropna(subset=["ยืนยันสิทธิ์"])
results = []

# 2. Forecast ทีละสาขา (Program-level)
for program, g in df.groupby("Major"):

    g = g.sort_values("Academic Year")
    if len(g) < 0:
        continue

    X = g["Academic Year"].values.reshape(-1, 1)
    y = g["ยืนยันสิทธิ์"].values

    # 3. ใช้ Linear Trend (Simple + Explainable)
    model = LinearRegression()
    model.fit(X, y)

    next_year = np.array([[g["Academic Year"].max() + 1]])
    forecast_demand = model.predict(next_year)[0]

    # 4. ปรับ Forecast ด้วย Historical Efficiency
    g["fill_rate"] = g["ยืนยันสิทธิ์"] / g["Plan"]  
    avg_fill_rate = g["fill_rate"].mean()

    recommended_intake = forecast_demand / max(avg_fill_rate, 0.6) 

    # 5. Guardrail กัน Forecast เพี้ยน
    last_enrolled = g["ยืนยันสิทธิ์"].iloc[-1]

    # จำกัดการเพิ่ม/ลด ไม่เกิน ±20% ต่อปี
    upper_bound = last_enrolled * 1.2
    lower_bound = last_enrolled * 0.8

    recommended_intake = np.clip(recommended_intake, lower_bound, upper_bound)

    results.append({
        "program": program,
        "plan": int(g["Plan"].iloc[-1]),
        "last_enrolled": int(last_enrolled),
        "forecast_demand": int(forecast_demand),
        "avg_fill_rate": round(avg_fill_rate, 2),
        "recommended_intake_next_year": int(recommended_intake),
        "academic 2026": int(next_year[0][0])
    })

# 6. Output Recommendation Table
forecast_df = pd.DataFrame(results)
print(forecast_df)
