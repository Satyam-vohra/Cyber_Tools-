import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

number = "+917983129514" 
phoneNumber = phonenumbers.parse(number)

Key = "d742f1b2f0ad4120aa2cef12ad6d8c27" 
yourLocation = geocoder.description_for_number(phoneNumber, "en")
print("Location: " + yourLocation)

yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
print("Service provider: " + yourServiceProvider)

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)
results = geocoder.geocode(query)

if results:
   
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")

    myMap = folium.Map(location=[lat, lng], zoom_start=9)

    folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

    myMap.save("Location.html")
    print("Map has been saved as 'Location.html'. Open it in your browser to view the location.")
else:
    print("No results found for the given location.")
