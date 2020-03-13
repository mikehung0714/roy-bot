from geopy import distance

location1 = (22.736251, 120.328874)
location2 = (22.724806, 120.331239)
print(distance.distance(location1, location2).km)