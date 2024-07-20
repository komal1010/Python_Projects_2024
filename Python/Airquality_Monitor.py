from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root=Tk()
root.title("Airquality_Monitor")
#root.iconbitmap('c:/Users/Garima Singh/Desktop/image.png')
root.geometry("600x80")
root.configure(background='yellow')

try:
	api_request= requests.get("https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode=85607&date=2024-07-19T00-0000&distance=25&API_KEY=4EF86D3B-B6B1-49BE-ADEE-AF060AB81FD4")
	api=json.loads(api_request.content)
	city=api[0]['ReportingArea']
	quality=api[0]['AQI']
	category=api[0]['Category']['Name']
except Exception as e:
	api="Error..."

myLabel= Label(root, text=city + " Air Quality" + str(quality) + " "+ category, font=("Helvetica", 30), background="yellow")
myLabel.pack()


root.mainloop()
