import requests
from bs4 import BeautifulSoup

def location(address):
	url = 'https://www.google.com/maps/search/?api=1&query=' + str(address)

	webContent = requests.get(url)
	#print(webContent.text)
	soup = BeautifulSoup(webContent.text,'lxml')
	coord = soup.findAll('meta',{'itemprop':'image'})[0]['content'].split('center=')[1].split('&')[0]
	lat = coord.split('%2C')[0]
	lon = coord.split('%2C')[1]

	return [lat,lon]

def getmaskData():
    url = 'https://quality.data.gov.tw/dq_download_csv.php?nid=116285&md5_url=2150b333756e64325bdbc4a5fd45fad1'
    web_data = requests.get(url)
    storeList = web_data.text.split('\n')
    storeList = [store.split(',') for store in web_data.text.split('\n')[1:] if store != '']
    resultList = ''
    for store in storeList[:100]:
        lat,lon = location(store[2])
        data = str(int(store[0])) + ',' + str(lat) + ',' + str(lon) + '\n'
        resultList += data
        print(data)
    with open('storeLatLon.csv',mode='w') as f:
        f.write(resultList)

getmaskData()