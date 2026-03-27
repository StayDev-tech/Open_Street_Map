# African Universities Map

## 📌 Description

This project visualizes universities in Central Africa, on an interactive map. It uses Python to fetch geographic coordinates from the OpenStreetMap Nominatim API, stores the data in SQLite, and generates a JavaScript file to display the universities on an OpenLayers map.

It is based on the **Python for Everybody (Py4E)** course project by Dr. Charles Severance (Dr Chuck), and has been modified to work with African university data.

It’s a simple, yet practical example of combining Python, databases, APIs, and web mapping, perfect for learning geocoding and data visualization while building a portfolio-ready project.
---

## 🚀 Features

* Fetches geographic data using a geocoding API
* Stores data in an SQLite database
* Generates a JavaScript file with coordinates
* Displays universities on an interactive OpenLayers map

---

## 🛠️ Technologies Used

* Python
* SQLite
* JavaScript (OpenLayers)
* HTML/CSS

---

## 📂 Project Structure

* `geoload.py` → Loads university data and fetches coordinates
* `geodump.py` → Extracts data and generates JavaScript file
* `universities.data` → List of universities
* `ca_universities.js` → Generated map data
* `where.html` → Map visualization

---

## ▶️ How to Run

1. Add universities in `universities.data`
2. Run:

   ```
   python geoload.py
   ```
3. Then run:

   ```
   python geodump.py
   ```
4. Open `where.html` in your browser

---

## ⚠️ Notes

* The `.sqlite` database file is ignored (not included in the repository)
* Make sure you have internet connection for geocoding

---

## 🙏 Acknowledgment

This project is adapted from the **Python for Everybody (Py4E)** course by Dr. Charles Severance.

---

## 👩🏽‍💻 Author

Stacey Kemgo
