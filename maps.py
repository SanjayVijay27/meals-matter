import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()

gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY'))

def find_distance(origin, destination):
    # Get distance matrix
    matrix = gmaps.distance_matrix(origins=origin, destinations=destination)

    # Return distance in miles
    try:
        return matrix['rows'][0]['elements'][0]['distance']['value'] / 1609.34
    except:
        return -1

# Test Google Maps API
if __name__ == '__main__':
    origin = "400 McCutcheon Dr, West Lafayette, Indiana, 47906"
    destination = "10 Juniper Hill Rd, Westford, Massachusetts, 01886"
    print(f"Distance: {find_distance(origin, destination)} meters")