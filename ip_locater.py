import webbrowser
import folium
import os
import requests

def locating_ip(ip_addr=""):
	own=requests.get("http://ip-api.com/json/")
	r=requests.get("http://ip-api.com/json/"+ip_addr)
	data=r.json()
	own_data=own.json()
	print(data)
	if data["status"]=="fail":
		if data["message"]=="invalid query":
			print("IP address doesnot exist")
		elif data["message"]=="private range":
			print("It is an Private Range IP address")
		print("Mapping to your default location")
		return(own_data["lat"],own_data["lon"],own_data["city"],own_data["country"],own_data["isp"])
	lat=data["lat"]
	lon=data["lon"]
	country=data["country"]
	city=data["city"]
	isp=data["isp"]
	return(lat,lon,city,country,isp)


def mark_on_map(lat,lon,city,org):
	ip_map=folium.Map(location=[lat,lon])
	tooltip="Click me"
	popup="<h2>"+city+"("+country+") belongs to "+org+"</h2>"
	folium.Marker([lat,lon],popup=popup,tooltip=tooltip).add_to(ip_map)
	ip_map.save("map.html")
	webbrowser.open("file://"+os.path.realpath("map.html"))
	return
	


print("Please provide the IP address")
ip_address=input()
latitude,longitude,city,country,organisation=locating_ip(ip_address)
mark_on_map(latitude,longitude,city,organisation)

