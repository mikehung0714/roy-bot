import requests
from bs4 import BeautifulSoup

def location(address):
	url = 'https://www.google.com/maps/search/?api=1&query=' + str(address)

	webContent = requests.get(url)
	soup = BeautifulSoup(webContent.text,'lxml')
	coord = soup.findAll('meta',{'itemprop':'image'})[0]['content'].split('center=')[1].split('&')[0]
	lat = coord.split('%2C')[0]
	lon = coord.split('%2C')[1]

	return [lat,lon]