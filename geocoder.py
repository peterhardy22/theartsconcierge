from geopy.geocoders import Nominatim

geolocator = Nominatim()

location = geolocator.geocode("omca")

print((location.latitude, location.longitude))
