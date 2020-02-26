import requests

def getMaskOpenData():
    url = 'https://quality.data.gov.tw/dq_download_csv.php?nid=116285&md5_url=2150b333756e64325bdbc4a5fd45fad1'

    web_data = requests.get(url)
    storeList = web_data.text.split('\n')

    storeList = [store.split(',') for store in web_data.text.split('\n')[1:] if store != '']

    storeList.sort(key=lambda x: int(x[4]), reverse=True)

    for store in storeList:
        addressList = store[2].split('縣')
        if len(addressList) == 1:
            store.append(store[2].split('市')[0] + '市')
        else:
            store.append(store[2].split('縣')[0] + '縣')
    return storeList