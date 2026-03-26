import streamlit as st
import random
import pandas as pd

st.title("Smart STP Monitoring System 🚧")

# -------------------------------
# 1. OVERLOADING MONITORING
# -------------------------------
st.header("⚙️ Overloading Monitoring")

load = st.slider("Current Load (%)", 0, 100)

if load < 70:
    st.success("🟢 Normal Load")
elif load < 85:
    st.warning("🟡 High Load Warning")
else:
    st.error("🔴 Critical Overload!")

st.metric("Current Load", f"{load}%")

# -------------------------------
# 2. INDUSTRIAL WASTE DETECTION
# -------------------------------
st.header("🧪 Industrial Waste Detection")

ph = st.slider("pH Level", 0.0, 14.0, 7.0)
tds = st.slider("TDS Level", 0, 2000)
turbidity = st.slider("Turbidity", 0, 100)

if ph < 5 or ph > 9 or tds > 1000 or turbidity > 50:
    st.error("⚠️ Industrial Waste Mixing Detected!")
else:
    st.success("✅ Water Quality Normal")

# -------------------------------
# 3. PREDICTION SYSTEM
# -------------------------------
st.header("📊 Load Prediction")

predicted_load = load + random.randint(-5, 15)

st.write(f"Predicted Load (Next Hour): {predicted_load}%")

if predicted_load > 85:
    st.error("⚠️ Future Overload Risk!")

# -------------------------------
# 4. VALVE CONTROL SYSTEM
# -------------------------------
st.header("🚰 Automated Valve Control")

if load > 85 or ph < 5 or ph > 9 or tds > 1000:
    st.error("🔴 Valve CLOSED (Unsafe Conditions)")
else:
    st.success("🟢 Valve OPEN (Safe)")

# -------------------------------
# 5. VIOLATION ALERT SYSTEM
# -------------------------------
st.header("🚨 Violations Log")

if load > 85:
    st.write("❌ Overloading violation detected")

if ph < 5 or ph > 9:
    st.write("❌ pH violation detected")

if tds > 1000:
    st.write("❌ Industrial discharge suspected")

# -------------------------------
# 6. GRAPH VISUALIZATION
# -------------------------------
st.header("📈 System Trend")

data = pd.DataFrame({
    "Load": [load, predicted_load]
})

st.line_chart(data)