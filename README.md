# Cyber_Tools-

📍 Phone Number Location Tracker

A simple Python project that extracts details from a phone number and visualizes its location on an interactive map.

🚀 Features

✅ Extract location of the phone number

✅ Detect the service provider (carrier)

✅ Fetch latitude & longitude using OpenCage Geocoder API

✅ Generate an interactive map with folium

✅ Save the map as Location.html for browser viewing

🛠️ Tech Stack

Python
phonenumbers
OpenCage Geocoder
folium

📦 Installation

Clone the repository and install dependencies:

git clone https://github.com/your-username/phone-number-tracker.git
cd phone-number-tracker
pip install phonenumbers opencage folium

🔑 API Key

This project uses the OpenCage Geocoder API.

Get your free API key from OpenCage
.

Replace the key in the script:

Key = "YOUR_API_KEY_HERE"

▶️ Usage
python tracker.py


Output:

Location details (city, region, etc.)
Service provider
Latitude & Longitude

Interactive map saved as Location.html

📸 Example Output
Location: India
Service provider: Airtel
Latitude: 28.6139, Longitude: 77.2090
Map has been saved as 'Location.html'.

🌍 Demo Map

The script generates an HTML map like this:

📜 License

This project is licensed under the MIT License.
