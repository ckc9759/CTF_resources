import requests

# Base API URL
BASE_URL = "https://numberchamp-challenge.utctf.live/match"
UUID = "7e9854e6-0fc8-41eb-b2e2-96e0ace559cf"

# Initial latitude and longitude
lat, lon = 39.940417100000076, -82.99669529999998 # Starting point
best_distance = float("inf")
closest_lat, closest_lon = lat, lon

def get_distance(lat, lon):
    url = f"{BASE_URL}?uuid={UUID}&lat={lat}&lon={lon}"
    response = requests.post(url)
    data = response.json()
    return data.get("distance", float("inf"))

# Optimization loop
step = 0.0000001  # Step size for changing lat/lon
for _ in range(100):  # Max iterations
    for dlat, dlon in [(step, 0), (-step, 0), (0, step), (0, -step)]:
        new_lat, new_lon = closest_lat + dlat, closest_lon + dlon
        distance = get_distance(new_lat, new_lon)
        
        if distance < best_distance:
            best_distance = distance
            closest_lat, closest_lon = new_lat, new_lon
            print(f"New closest: {closest_lat}, {closest_lon} -> Distance: {best_distance}")

print(f"Final closest match: {closest_lat}, {closest_lon} -> Distance: {best_distance}")
