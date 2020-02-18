import requests

url = 'http://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D50001-001&l=https://data.nhi.gov.tw/resource/mask/maskdata.csv'

r = requests.get(url)
r.encoding = 'UTF-8'
content = r.text

storeList = list(csv.reader(web_data.text.split('\n'), delimiter=','))
storeList = sorted(storeList,key=lambda x:int(x[4]), reverse=True)
print(storeList[0])
print(storeList[1])
print(storeList[2])
