import requests
from geopy import distance

from function.location import location

def getMaskOpenData(userLocation,userlat,userlon):
    url = 'https://quality.data.gov.tw/dq_download_csv.php?nid=116285&md5_url=2150b333756e64325bdbc4a5fd45fad1'

    web_data = requests.get(url)
    storeList = web_data.text.split('\n')

    storeList = [store.split(',') for store in web_data.text.split('\n')[1:] if store != '']

    tempList = []

    for store in storeList:
        county = ''
        addressList = store[2].split('縣')
        if len(addressList) == 1:
            county = store[2].split('市')[0] + '市'
            if '臺' in county:
                county.replace('臺','台')
            store.append(county)
        else:
            county = store[2].split('縣')[0] + '縣'
            if '臺' in county:
                county.replace('臺','台')
            store.append(county)
        
        if county == userLocation:
            tempList.append(store)
    
    tempList = [store for store in tempList if int(store[4]) > 500 and int(store[5]) > 500]
    # tempList.sort(key = lambda x : int(x[4]) + int(x[5]),reverse=True)
    print('有{}家藥局'.format(len(tempList)))
    resultList = []
    for store in tempList:
        storelat,storelon = location(store[2])
        store.append(distance.distance((storelat,storelon),(userlat,userlon)).km)
        resultList.append(store)

    resultList.sort(key = lambda x:float(x[-1]))

    if len(resultList) > 10:
        return resultList[:10]
    else:
        return resultList

# print(getMaskOpenData())