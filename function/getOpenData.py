import requests

def getMaskOpenData():
    url = 'https://quality.data.gov.tw/dq_download_csv.php?nid=116285&md5_url=2150b333756e64325bdbc4a5fd45fad1'

    web_data = requests.get(url)
    storeList = web_data.text.split('\n')

    storeList = [store.split(',') for store in web_data.text.split('\n')[1:] if store != '']

    storeList.sort(key=lambda x: int(x[4]), reverse=True)

    return storeList[0][2]
    # print(storeList[1][2])
    # print(storeList[2][2])

#print(getMaskOpenData())