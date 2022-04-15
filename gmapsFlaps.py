import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBX-Dhd5ngtvA8LP54KTE8NfOzSqxhs4rM')


print(gmaps)

geocode_result = gmaps.geocode('singapore 018956')

print(geocode_result[0]["formatted_address"])