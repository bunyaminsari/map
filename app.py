import folium
from numpy import arccosh
import pandas
from geopy import ArcGIS
nom = ArcGIS()

print("Please enter your address accordingly!")
address = input("Address: ")
city = input("City: ")
state = input("State: ")
zip = input("Zip: ")

df = pandas.DataFrame([[address,city,state,zip]],columns=["address","city","state","zip"])
df["Full Address"] = df["address"]+","+df["city"]+","+df["state"]+ ","+ str(df["zip"])
df["Coordinates"] = df["Full Address"].apply(nom.geocode)
latitude = df["Latitude"] = df["Coordinates"].apply(lambda la : la.latitude if la != None else None)
longitude = df["Longitude"] = df["Coordinates"].apply(lambda lo : lo.longitude if lo != None else None)


map = folium.Map(location=[latitude,longitude])
map.save("map1.html")

