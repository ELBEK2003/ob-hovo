import requests
from pprint import pprint
from telegram import Update
from telegram.ext import CallbackContext


def get_data(lat,long):

	url = "https://yahoo-weather5.p.rapidapi.com/weather"

	querystring = {"lat":f"{lat}","long":f"{long}","format":"json","u":"c"}

	headers = {
		"X-RapidAPI-Key": "fafd5a08d0mshb25eb8bf2f5f7e7p10e061jsn6d08cbeff10b",
		"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
	}
	data={}
	response = requests.request("GET", url, headers=headers, params=querystring)
	data["sunrise"]=response.json()['current_observation']['astronomy']['sunrise']
	data["sunset"]=response.json()['current_observation']['astronomy']['sunset']
	data["namlik"]=response.json()['current_observation']['atmosphere']['humidity']
	data["temp"]=response.json()['current_observation']['condition']['temperature']
	data["condition"]=response.json()['current_observation']['condition']['text']
	data["wind_speed"]=response.json()['current_observation']['wind']['speed']
	data["city"]=response.json()['location']['city']
	data["country"] = response.json()['location']['country']
	return data


import requests

url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

headers = {
	"X-RapidAPI-Key": "fafd5a08d0mshb25eb8bf2f5f7e7p10e061jsn6d08cbeff10b",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)