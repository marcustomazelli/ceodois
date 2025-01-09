
# 🌳 CEODOIS

![img-ceodois](/static/img/img-logo/gif.gif)


![CEODOIS](https://img.shields.io/badge/Sustentabilidade%20e%20Tecnologia-green)  
CEODOIS is a web application that helps users understand and reduce their carbon footprint. It also provides real-time monitoring of Brazil fires using NASA satellite data.

---

## 📋 **Features**

### 🧮 **CO₂ Emissions Calculator**
- Allows the user to enter monthly consumption data (fuel, electricity, cooking gas, etc.).
- Calculates individual or family carbon footprint.
- Shows impactful comparisons, such as:
  - How many trees would be needed to neutralize emissions?
  - How many liters of polar ice would melt?
  - How many kilometers of fuel-efficient car is the emission equivalent to?
  - How many square meters of burnt forest equals emissions?

### 🔥 **Burn Monitoring**
- Uses NASA's FIRMS API to monitor fires in real-time.
- Displays data on an interactive map with markers for:
  - Location of the fires.
  - Fire intensity.
  - Detection confidence.

### 📱 **Sharing on Instagram Stories** (FEATURE DESIRED)
- Captures the calculator's results and allows users to share them on Instagram Stories.

---


## 🚀 **Technologies Used**
- Frontend
  - HTML, CSS, JavaScript
  - Library [LeafletJS](https://leafletjs.com/) for interactive maps.
- **Backend:**
  - Flask (Python) for routes and data processing.
  - pandas
  - JSON
  - Integration with external APIs (NASA FIRMS).
- APIs:**
  - [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) for fire data.
