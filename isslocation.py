import json
import urllib.request
import turtle


url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("People in space station: ", result['number'])
people = result['people']
for p in people:
    print (p['name'])


url_loc = 'http://api.open-notify.org/iss-now.json'
resp = urllib.request.urlopen(url_loc)
res_loc = json.loads(resp.read())
location = res_loc["iss_position"]
lat = location['latitude']
lon = location['longitude']
print ("Latitude: ",lat)
print ("Longitude: ",lon)


screen = turtle.Screen()
screen.setup(720, 360)
# screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic(r'C:\Users\Neil Dahiya\PycharmProjects\Space Station Location\map.jpg')

screen.register_shape('satellite.png')
iss = turtle.Turtle()
iss.shape('satellite.png')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)